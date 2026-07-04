"""WSGI config for Medicenters Performance."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
application = get_wsgi_application()
