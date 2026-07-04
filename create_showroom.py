import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
import django
django.setup()

from apps.core.models import Showroom

s, created = Showroom.objects.get_or_create(
    slug='kinedoc-tanger',
    defaults={
        'title': 'Cabinet KineDoc - Tanger',
        'description': 'Visite virtuelle 3D du cabinet KineDoc, un projet realise par MEDICENTERS PERFORMANCE.',
        'matterport_embed_url': 'https://my.matterport.com/show/?m=example123',
        'is_active': True,
        'is_featured': True,
        'ordering': 1,
    }
)
status = "created" if created else "already exists"
print(f"Showroom {status}: {s.title}")
