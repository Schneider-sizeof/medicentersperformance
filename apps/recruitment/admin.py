"""Admin configuration for recruitment app."""
from django.contrib import admin
from django.utils.html import format_html

from .models import JobPosting, Application


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'contract_type', 'location', 'is_active', 'posted_date')
    list_filter = ('is_active', 'contract_type', 'department')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
    readonly_fields = ('posted_date',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'position', 'submitted_at', 'is_reviewed', 'cv_link')
    list_filter = ('is_reviewed', 'submitted_at', 'position')
    search_fields = ('full_name', 'email')
    list_editable = ('is_reviewed',)
    readonly_fields = ('submitted_at',)
    date_hierarchy = 'submitted_at'

    @admin.display(description='CV')
    def cv_link(self, obj):
        if obj.cv_file:
            return format_html(
                '<a href="{}" target="_blank">📄 Télécharger</a>',
                obj.cv_file.url,
            )
        return '—'
