"""URL configuration for Medicenters Performance."""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from apps.core.sitemaps import StaticSitemap, BlogSitemap, JobSitemap

sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap,
    'jobs': JobSitemap,
}

# Non-i18n URL patterns (sitemap, robots, ckeditor, language switch)
urlpatterns = [
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap',
    ),
    path(
        'robots.txt',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
        name='robots_txt',
    ),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Internationalized URL patterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path(_('services/'), include('apps.services.urls')),
    path(_('blog/'), include('apps.blog.urls')),
    path(_('recruitment/'), include('apps.recruitment.urls')),
    path(_('contact/'), include('apps.contact.urls')),
    path(_('partner/'), include('apps.partnership.urls')),
    prefix_default_language=True,
)

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

