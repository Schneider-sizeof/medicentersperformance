"""Admin configuration for core app."""
from django.contrib import admin
from .models import CompanyInfo, Testimonial, Showroom

# ---------------------------------------------------------------------------
# Customize admin site branding
# ---------------------------------------------------------------------------
admin.site.site_header = 'MEDICENTERS PERFORMANCE — Administration'
admin.site.site_title = 'Medicenters Admin'
admin.site.index_title = 'Gestion du site'


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    """Singleton company info — only one instance allowed."""

    fieldsets = (
        ('Contact', {
            'fields': ('phone', 'email', 'address'),
        }),
        ('Horaires', {
            'fields': ('hours_weekday', 'hours_saturday'),
        }),
        ('Réseaux sociaux', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url', 'youtube_url'),
        }),
        ('Carte', {
            'fields': ('google_maps_embed_url',),
        }),
    )

    def has_add_permission(self, request):
        """Only allow one CompanyInfo instance."""
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_role', 'company', 'is_active', 'ordering')
    list_editable = ('is_active', 'ordering')
    list_filter = ('is_active',)
    search_fields = ('client_name', 'company', 'content')


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'is_active', 'ordering')
    list_editable = ('is_featured', 'is_active', 'ordering')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_featured', 'is_active')
