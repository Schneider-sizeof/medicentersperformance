"""Core views — Home and About pages."""
from django.shortcuts import render
from .models import Testimonial, Showroom


def home(request):
    """Render the home page with services, testimonials, and featured showroom."""
    from apps.services.models import Service
    from apps.blog.models import BlogPost

    context = {
        'services': Service.objects.filter(is_active=True),
        'testimonials': Testimonial.objects.filter(is_active=True),
        'showrooms': Showroom.objects.filter(is_active=True).order_by('ordering'),
        'featured_showroom': Showroom.objects.filter(
            is_featured=True, is_active=True
        ).first(),
        'recent_posts': BlogPost.objects.filter(
            is_published=True
        ).order_by('-published_date')[:3],
    }
    return render(request, 'core/home.html', context)


def about(request):
    """Render the About Us page."""
    return render(request, 'core/about.html')
