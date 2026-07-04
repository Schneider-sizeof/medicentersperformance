"""Model translation registration for blog app."""
from modeltranslation.translator import translator, TranslationOptions
from .models import Category, BlogPost


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'content', 'meta_description', 'featured_image_alt')


translator.register(Category, CategoryTranslationOptions)
translator.register(BlogPost, BlogPostTranslationOptions)
