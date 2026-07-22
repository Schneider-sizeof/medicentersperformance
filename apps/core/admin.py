"""Admin configuration for core app."""
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CompanyInfo, Testimonial, Showroom, Partner, ShowroomGalleryImage

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
        ('Intégrations & SEO', {
            'fields': ('google_analytics_id', 'google_search_console_id'),
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


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview', 'website_url', 'is_active', 'ordering')
    list_display_links = ('name',)
    list_filter = ('is_active',)
    search_fields = ('name',)

    @admin.display(description='Logo')
    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height:30px;max-width:80px;object-fit:contain;" />')
        return '—'


@admin.register(ShowroomGalleryImage)
class ShowroomGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title_preview', 'image_preview', 'is_active', 'ordering')
    list_editable = ('is_active', 'ordering')
    list_filter = ('is_active',)

    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 40px; border-radius: 4px;" />')
        return '—'

    @admin.display(description='Titre')
    def title_preview(self, obj):
        return obj.title or f"Image #{obj.id}"

