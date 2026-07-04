"""Admin configuration for partnership app."""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import PartnershipInquiry


@admin.register(PartnershipInquiry)
class PartnershipInquiryAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_person', 'email', 'phone', 'city', 'is_read', 'created_at')
    list_filter = ('is_read', 'country', 'created_at')
    search_fields = ('company_name', 'contact_person', 'email', 'city', 'activity_sector')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (_('Informations entreprise'), {
            'fields': ('company_name', 'contact_person', 'position', 'email', 'phone'),
        }),
        (_('Localisation'), {
            'fields': ('country', 'city', 'company_website'),
        }),
        (_('Détails entreprise'), {
            'fields': ('activity_sector', 'years_in_business', 'num_employees'),
        }),
        (_('Demande'), {
            'fields': ('products_of_interest', 'message'),
        }),
        (_('Statut'), {
            'fields': ('is_read', 'created_at'),
        }),
    )
