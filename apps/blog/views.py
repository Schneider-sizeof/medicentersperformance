"""Blog views — post list with pagination/filter and post detail."""
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, Category


def post_list(request):
    """List published blog posts with optional category filtering and pagination."""
    posts = BlogPost.objects.filter(is_published=True)
    categories = Category.objects.all()
    current_category = request.GET.get('category')

    if current_category:
        posts = posts.filter(category__slug=current_category)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'posts': page_obj,
        'categories': categories,
        'current_category': current_category,
    })


def post_detail(request, slug):
    """Display a single blog post with related posts."""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    # Related posts: same category, exclude current, limit 3
    related_posts = BlogPost.objects.filter(
        is_published=True, category=post.category
    ).exclude(pk=post.pk)[:3] if post.category else BlogPost.objects.none()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'related_posts': related_posts,
    })
