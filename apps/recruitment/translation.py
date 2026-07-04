"""Model translation registration for recruitment app."""
from modeltranslation.translator import translator, TranslationOptions
from .models import JobPosting


class JobPostingTranslationOptions(TranslationOptions):
    fields = ('title', 'department', 'location', 'description', 'requirements')


translator.register(JobPosting, JobPostingTranslationOptions)
