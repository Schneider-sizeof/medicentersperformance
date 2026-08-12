"""Sitemaps for SEO — covers static pages, blog posts, and job listings."""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.blog.models import BlogPost
from apps.recruitment.models import JobPosting


class StaticSitemap(Sitemap):
    """Sitemap for static pages (home, about, services, contact, recruitment)."""
    protocol = 'https'
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['core:home', 'core:about', 'services:list', 'contact:contact', 'recruitment:careers', 'partnership:partnership']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    """Sitemap for published blog posts."""
    protocol = 'https'
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class JobSitemap(Sitemap):
    """Sitemap for active job postings."""
    protocol = 'https'
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return JobPosting.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.posted_date

    def location(self, obj):
        return obj.get_absolute_url()
