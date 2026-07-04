"""Admin configuration for services app — Products and Services with image previews."""
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Product, Service, ServiceImage


def _image_preview(image_field, alt=''):
    """Return an HTML image thumbnail or a dash if no image."""
    if image_field:
        return format_html(
            '<img src="{}" alt="{}" style="height:60px;width:auto;border-radius:6px;object-fit:cover;">',
            image_field.url, alt,
        )
    return '—'


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1
    fields = ('image', 'alt_text', 'caption', 'ordering')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image1', 'ordering', 'is_active', 'updated_at')
    list_editable = ('ordering', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('preview_image1_large', 'preview_image2_large', 'preview_image3_large', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'slug', 'is_active', 'ordering'),
        }),
        (_('Image 1'), {
            'fields': ('image1', 'image1_alt', 'preview_image1_large'),
        }),
        (_('Image 2'), {
            'fields': ('image2', 'image2_alt', 'preview_image2_large'),
        }),
        (_('Image 3'), {
            'fields': ('image3', 'image3_alt', 'preview_image3_large'),
        }),
    )

    @admin.display(description=_('Aperçu'))
    def preview_image1(self, obj):
        return _image_preview(obj.image1, obj.image1_alt)

    @admin.display(description=_('Aperçu Image 1'))
    def preview_image1_large(self, obj):
        if obj.image1:
            return format_html(
                '<img src="{}" alt="{}" style="max-height:200px;border-radius:8px;">',
                obj.image1.url, obj.image1_alt,
            )
        return _('Aucune image téléchargée')

    @admin.display(description=_('Aperçu Image 2'))
    def preview_image2_large(self, obj):
        if obj.image2:
            return format_html(
                '<img src="{}" alt="{}" style="max-height:200px;border-radius:8px;">',
                obj.image2.url, obj.image2_alt,
            )
        return _('Aucune image téléchargée')

    @admin.display(description=_('Aperçu Image 3'))
    def preview_image3_large(self, obj):
        if obj.image3:
            return format_html(
                '<img src="{}" alt="{}" style="max-height:200px;border-radius:8px;">',
                obj.image3.url, obj.image3_alt,
            )
        return _('Aucune image téléchargée')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'preview_image1', 'ordering', 'is_active', 'updated_at')
    list_editable = ('ordering', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle', 'short_description')
    inlines = [ServiceImageInline]
    readonly_fields = ('preview_image1_large', 'preview_image2_large', 'preview_image3_large', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'slug', 'icon_class', 'is_active', 'ordering'),
        }),
        (_('Contenu'), {
            'fields': ('short_description', 'long_description'),
        }),
        (_('Image principale (ancienne)'), {
            'fields': ('image', 'image_alt'),
            'classes': ('collapse',),
        }),
        (_('Image 1'), {
            'fields': ('image1', 'image1_alt', 'preview_image1_large'),
        }),
        (_('Image 2'), {
            'fields': ('image2', 'image2_alt', 'preview_image2_large'),
        }),
        (_('Image 3'), {
            'fields': ('image3', 'image3_alt', 'preview_image3_large'),
        }),
    )

    @admin.display(description=_('Aperçu'))
    def preview_image1(self, obj):
        return _image_preview(obj.image1, obj.image1_alt)

    @admin.display(description=_('Aperçu Image 1'))
    def preview_image1_large(self, obj):
        if obj.image1:
            return format_html(
                '<img src="{}" alt="{}" style="max-height:200px;border-radius:8px;">',
                obj.image1.url, obj.image1_alt,
            )
        return _('Aucune image téléchargée')

    @admin.display(description=_('Aperçu Image 2'))
    def preview_image2_large(self, obj):
        if obj.image2:
            return format_html(
                '<img src="{}" alt="{}" style="max-height:200px;border-radius:8px;">',
                obj.image2.url, obj.image2_alt,
            )
        return _('Aucune image téléchargée')

    @admin.display(description=_('Aperçu Image 3'))
    def preview_image3_large(self, obj):
        if obj.image3:
            return format_html(
                '<img src="{}" alt="{}" style="max-height:200px;border-radius:8px;">',
                obj.image3.url, obj.image3_alt,
            )
        return _('Aucune image téléchargée')
