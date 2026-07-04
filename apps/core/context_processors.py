"""Context processors for global template variables."""
from django.conf import settings


def company_info(request):
    """Make company info, active services, and language data available to all templates."""
    from .models import CompanyInfo
    from apps.services.models import Service

    try:
        info = CompanyInfo.get_instance()
    except Exception:
        info = None

    try:
        services = Service.objects.filter(is_active=True).order_by('ordering')
    except Exception:
        services = []

    current_language = getattr(request, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)

    return {
        'company': info,
        'footer_services': services,
        'is_rtl': current_language == 'ar',
        'current_language': current_language,
        'available_languages': settings.LANGUAGES,
        'site_name': 'MEDICENTERS PERFORMANCE',
    }
