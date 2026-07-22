import os
import logging
from django.http import HttpResponseForbidden

logger = logging.getLogger('django.security')

class AdminIPAllowlistMiddleware:
    """
    Middleware to restrict access to the Django Admin panel based on client IP.
    Configure allowed IPs using the ADMIN_IP_ALLOWLIST environment variable (comma-separated).
    If ADMIN_IP_ALLOWLIST is empty/unset, access is permitted to all IPs.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info.lstrip('/')
        
        # Get dynamic admin url path
        admin_url = os.environ.get('DJANGO_ADMIN_URL', 'dashboard_medicenters/')
        if not admin_url.endswith('/'):
            admin_url += '/'
            
        if path.startswith(admin_url):
            allowlist_str = os.environ.get('ADMIN_IP_ALLOWLIST', '')
            if allowlist_str:
                allowed_ips = [ip.strip() for ip in allowlist_str.split(',') if ip.strip()]
                
                # Check X-Forwarded-For if behind a proxy like PythonAnywhere/cPanel/Cloudflare
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0].strip()
                else:
                    ip = request.META.get('REMOTE_ADDR')
                
                if ip not in allowed_ips:
                    logger.warning(
                        f"Blocked unauthorized admin access attempt to /{path} from IP: {ip} (User-Agent: {request.META.get('HTTP_USER_AGENT', 'Unknown')})"
                    )
                    return HttpResponseForbidden("Access Denied: Your IP address is not authorized to access this page.")
                    
        return self.get_response(request)
