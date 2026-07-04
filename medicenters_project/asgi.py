"""ASGI config for Medicenters Performance."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
application = get_asgi_application()
