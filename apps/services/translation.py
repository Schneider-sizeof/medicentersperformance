"""Model translation registration for services app."""
from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Service


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'image1_alt', 'image2_alt', 'image3_alt')


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'short_description', 'long_description', 'image_alt', 'image1_alt', 'image2_alt', 'image3_alt')


translator.register(Product, ProductTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
