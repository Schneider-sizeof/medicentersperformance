"""Services app models — products, services, and gallery images."""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """
    A product offered by MEDICENTERS PERFORMANCE.
    Each instance is a card on the Produits & Services page, manageable from admin.
    """
    title = models.CharField(_('Titre'), max_length=200)
    subtitle = models.CharField(
        _('Sous-titre'), max_length=300, blank=True,
        help_text=_('Courte description affichée sous le titre'),
    )
    slug = models.SlugField(_('Slug'), unique=True)
    image1 = models.ImageField(
        _('Image 1'), upload_to='products/', blank=True, null=True,
    )
    image1_alt = models.CharField(_('Texte alternatif image 1'), max_length=150, blank=True)
    image2 = models.ImageField(
        _('Image 2'), upload_to='products/', blank=True, null=True,
    )
    image2_alt = models.CharField(_('Texte alternatif image 2'), max_length=150, blank=True)
    image3 = models.ImageField(
        _('Image 3'), upload_to='products/', blank=True, null=True,
    )
    image3_alt = models.CharField(_('Texte alternatif image 3'), max_length=150, blank=True)
    ordering = models.PositiveIntegerField(_('Ordre'), default=0)
    is_active = models.BooleanField(_('Actif'), default=True)
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('Produit')
        verbose_name_plural = _('Produits')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{reverse('services:list')}#product-{self.slug}"


class Service(models.Model):
    """
    A service category offered by MEDICENTERS PERFORMANCE.
    Each instance is a section on the Services page, manageable from admin.
    """
    title = models.CharField(_('Titre'), max_length=200)
    subtitle = models.CharField(
        _('Sous-titre'), max_length=300, blank=True,
        help_text=_('Courte description affichée sous le titre'),
    )
    slug = models.SlugField(_('Slug'), unique=True)
    icon_class = models.CharField(
        _('Classe d\'icône'), max_length=50, blank=True,
        help_text=_('Classe Bootstrap Icons, ex : bi-building'),
    )
    short_description = models.TextField(
        _('Description courte'),
        help_text=_('Pour les cartes résumées (1-2 phrases)'),
    )
    long_description = models.TextField(
        _('Description détaillée'),
        help_text=_('Description complète affichée sur la page Services'),
    )
    image = models.ImageField(
        _('Image principale'), upload_to='services/', blank=True, null=True,
    )
    image_alt = models.CharField(_('Texte alternatif image principale'), max_length=150, blank=True)
    image1 = models.ImageField(
        _('Image 1'), upload_to='services/', blank=True, null=True,
    )
    image1_alt = models.CharField(_('Texte alternatif image 1'), max_length=150, blank=True)
    image2 = models.ImageField(
        _('Image 2'), upload_to='services/', blank=True, null=True,
    )
    image2_alt = models.CharField(_('Texte alternatif image 2'), max_length=150, blank=True)
    image3 = models.ImageField(
        _('Image 3'), upload_to='services/', blank=True, null=True,
    )
    image3_alt = models.CharField(_('Texte alternatif image 3'), max_length=150, blank=True)
    ordering = models.PositiveIntegerField(_('Ordre'), default=0)
    is_active = models.BooleanField(_('Actif'), default=True)
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{reverse('services:list')}#service-{self.slug}"


class ServiceImage(models.Model):
    """Gallery image for a Service, shown on the detailed service section."""
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='gallery_images',
        verbose_name=_('Service'),
    )
    image = models.ImageField(_('Image'), upload_to='services/gallery/')
    alt_text = models.CharField(_('Texte alternatif'), max_length=150)
    caption = models.CharField(_('Légende'), max_length=200, blank=True)
    ordering = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('Image de service')
        verbose_name_plural = _('Images de service')

    def __str__(self):
        return f'{self.service.title} — {self.alt_text}'
