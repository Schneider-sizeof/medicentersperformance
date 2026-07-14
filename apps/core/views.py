"""Core views — Home and About pages."""
from django.shortcuts import render
from .models import Testimonial, Showroom, Partner


def home(request):
    """Render the home page with services, testimonials, and featured showroom."""
    from apps.services.models import Service, Product
    from apps.blog.models import BlogPost

    class CuratedService:
        def __init__(self, title, short_description, icon_class, absolute_url):
            self.title = title
            self.short_description = short_description
            self.icon_class = icon_class
            self.absolute_url = absolute_url

        def get_absolute_url(self):
            return self.absolute_url

    # Curate the 9 items in the exact same list/order as the footer
    curated_items = []

    # 1. Architecture d'intérieur (Service)
    s_arch = Service.objects.filter(slug='architecture-interieur', is_active=True).first()
    if s_arch:
        curated_items.append(CuratedService(
            s_arch.title, s_arch.short_description, s_arch.icon_class or 'bi-house-heart', s_arch.get_absolute_url()
        ))

    # 2. Mobilier médical modulaire (Product)
    p_mob = Product.objects.filter(slug='mobilier-medical-modulaire', is_active=True).first()
    if p_mob:
        curated_items.append(CuratedService(
            p_mob.title, p_mob.subtitle, 'bi-clipboard-pulse', p_mob.get_absolute_url()
        ))

    # 3. Comptoir d'accueil (Product)
    p_comp = Product.objects.filter(slug='comptoir-accueil', is_active=True).first()
    if p_comp:
        curated_items.append(CuratedService(
            p_comp.title, p_comp.subtitle, 'bi-person-workspace', p_comp.get_absolute_url()
        ))

    # 4. Portes & cloisons (Product)
    p_portes = Product.objects.filter(slug='portes-cloisons', is_active=True).first()
    if p_portes:
        curated_items.append(CuratedService(
            p_portes.title, p_portes.subtitle, 'bi-door-closed', p_portes.get_absolute_url()
        ))

    # 5. Enseignes publicitaires (Product)
    p_ens = Product.objects.filter(slug='enseignes-publicitaires', is_active=True).first()
    if p_ens:
        curated_items.append(CuratedService(
            p_ens.title, p_ens.subtitle, 'bi-signpost-split', p_ens.get_absolute_url()
        ))

    # 6. Logiciel de gestion (Product)
    p_log = Product.objects.filter(slug='logiciel-gestion', is_active=True).first()
    if p_log:
        curated_items.append(CuratedService(
            p_log.title, p_log.subtitle, 'bi-laptop', p_log.get_absolute_url()
        ))

    # 7. Aménagement PMR (Service)
    s_pmr = Service.objects.filter(slug='amenagement-pmr', is_active=True).first()
    if s_pmr:
        curated_items.append(CuratedService(
            s_pmr.title, s_pmr.short_description, s_pmr.icon_class or 'bi-universal-access', s_pmr.get_absolute_url()
        ))

    # 8. Coaching et formation (Service)
    s_coach = Service.objects.filter(slug='coaching-formation', is_active=True).first()
    if s_coach:
        curated_items.append(CuratedService(
            s_coach.title, s_coach.short_description, s_coach.icon_class or 'bi-journal-check', s_coach.get_absolute_url()
        ))

    # 9. Création de sites web (Service)
    s_web = Service.objects.filter(slug='creation-site-web', is_active=True).first()
    if s_web:
        curated_items.append(CuratedService(
            s_web.title, s_web.short_description, s_web.icon_class or 'bi-globe', s_web.get_absolute_url()
        ))

    context = {
        'services': curated_items,
        'testimonials': Testimonial.objects.filter(is_active=True),
        'showrooms': Showroom.objects.filter(is_active=True).order_by('ordering'),
        'featured_showroom': Showroom.objects.filter(
            is_featured=True, is_active=True
        ).first(),
        'partners': Partner.objects.filter(is_active=True),
        'recent_posts': BlogPost.objects.filter(
            is_published=True
        ).order_by('-published_date')[:3],
    }
    return render(request, 'core/home.html', context)


def about(request):
    """Render the About Us page."""
    return render(request, 'core/about.html')

