"""Admin configuration for blog app."""
from django import forms
from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Category, BlogPost


class BlogPostAdminForm(forms.ModelForm):
    """Apply CKEditor5 widget to all translated content fields."""

    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='extends'),
            'content_fr': CKEditor5Widget(config_name='extends'),
            'content_ar': CKEditor5Widget(config_name='extends'),
            'content_en': CKEditor5Widget(config_name='extends'),
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'category', 'author', 'is_published', 'published_date')
    list_filter = ('is_published', 'category', 'published_date')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    date_hierarchy = 'published_date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'category'),
        }),
        ('Contenu', {
            'fields': ('excerpt', 'content'),
        }),
        ('Image', {
            'fields': ('featured_image', 'featured_image_alt'),
        }),
        ('SEO', {
            'fields': ('meta_description',),
        }),
        ('Publication', {
            'fields': ('is_published', 'published_date'),
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    actions = ['make_published', 'make_unpublished']

    @admin.action(description='Publier les articles sélectionnés')
    def make_published(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description='Dépublier les articles sélectionnés')
    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)
