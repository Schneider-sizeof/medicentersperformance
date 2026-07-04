"""Admin configuration for contact app."""
from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'subject'),
        }),
        ('Message', {
            'fields': ('message',),
        }),
        ('Statut', {
            'fields': ('is_read', 'created_at'),
        }),
    )
