"""Blog app models — categories and blog posts with rich text content."""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Blog post category for filtering and organization."""
    name = models.CharField(_('Nom'), max_length=100)
    slug = models.SlugField(_('Slug'), unique=True)

    class Meta:
        verbose_name = _('Catégorie')
        verbose_name_plural = _('Catégories')
        ordering = ['name']

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """
    Blog article with rich text content (CKEditor 5 via admin widget).
    Supports full SEO metadata and multi-language translations.
    """
    title = models.CharField(_('Titre'), max_length=250)
    slug = models.SlugField(_('Slug'), unique=True, max_length=260)
    excerpt = models.TextField(
        _('Extrait'), max_length=300,
        help_text=_('Résumé court pour les listes et le SEO'),
    )
    content = models.TextField(_('Contenu'))
    featured_image = models.ImageField(
        _('Image à la une'), upload_to='blog/', blank=True, null=True,
    )
    featured_image_alt = models.CharField(
        _('Texte alternatif image'), max_length=150, blank=True,
    )
    author = models.CharField(
        _('Auteur'), max_length=100, default='MEDICENTERS PERFORMANCE',
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='posts', verbose_name=_('Catégorie'),
    )
    meta_description = models.CharField(
        _('Méta-description SEO'), max_length=160, blank=True,
        help_text=_('Description pour les moteurs de recherche (max 160 caractères)'),
    )
    is_published = models.BooleanField(_('Publié'), default=False)
    published_date = models.DateTimeField(_('Date de publication'), null=True, blank=True)
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Mis à jour le'), auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = _('Article de blog')
        verbose_name_plural = _('Articles de blog')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
