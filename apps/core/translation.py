"""Model translation registration for core app."""
from modeltranslation.translator import translator, TranslationOptions
from .models import CompanyInfo, Testimonial, Showroom


class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('address', 'hours_weekday', 'hours_saturday')


class TestimonialTranslationOptions(TranslationOptions):
    fields = ('client_name', 'client_role', 'company', 'content')


class ShowroomTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(CompanyInfo, CompanyInfoTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(Showroom, ShowroomTranslationOptions)
