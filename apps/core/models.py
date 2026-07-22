"""Core app models — site-wide settings, testimonials, Matterport showrooms."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class CompanyInfo(models.Model):
    """
    Singleton model for site-wide company information.
    Managed from the Django admin — avoids hardcoding contact details in templates.
    """
    phone = models.CharField(
        _('Téléphone'), max_length=20, default='+212 660 78 50 38'
    )
    email = models.EmailField(
        _('Email'), default='contact@medicenters.ma'
    )
    address = models.TextField(
        _('Adresse'),
        default='Boulevard Mohammed V, Résidence Redouane Chirine 112 N°48, Tanger, Morocco',
    )
    hours_weekday = models.CharField(
        _('Horaires semaine'), max_length=100,
        default='Lundi–Vendredi 09:00–20:00',
    )
    hours_saturday = models.CharField(
        _('Horaires samedi'), max_length=100,
        default='Samedi 09:00–15:00',
    )
    facebook_url = models.URLField(_('Facebook'), blank=True, default='https://facebook.com/medicenters')
    instagram_url = models.URLField(_('Instagram'), blank=True, default='https://instagram.com/medicenters_performance')
    linkedin_url = models.URLField(_('LinkedIn'), blank=True, default='https://linkedin.com/company/medicenters')
    youtube_url = models.URLField(_('YouTube'), blank=True, default='https://youtube.com/@medicenters')
    google_maps_embed_url = models.URLField(
        _('URL Google Maps (embed)'),
        blank=True,
        help_text=_('URL iframe src pour la carte Google Maps sur la page Contact'),
    )
    google_analytics_id = models.CharField(
        _('ID Google Analytics'),
        max_length=50,
        blank=True,
        help_text=_('Ex : G-XXXXXXX. Laissez vide pour désactiver le suivi.'),
    )
    google_search_console_id = models.CharField(
        _('ID Google Search Console'),
        max_length=100,
        blank=True,
        help_text=_('Code de vérification Google Search Console (le code dans le champ content="..."). Laissez vide pour désactiver.'),
    )

    class Meta:
        verbose_name = _('Informations entreprise')
        verbose_name_plural = _('Informations entreprise')

    def __str__(self):
        return 'MEDICENTERS PERFORMANCE'

    def save(self, *args, **kwargs):
        """Enforce singleton: always save with pk=1."""
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Prevent deletion of the singleton."""
        pass  # noqa: WPS420

    @classmethod
    def get_instance(cls):
        """Return the singleton instance, creating it with defaults if needed."""
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj


class Testimonial(models.Model):
    """Client testimonial, managed from the admin."""
    client_name = models.CharField(_('Nom du client'), max_length=100)
    client_role = models.CharField(
        _('Fonction'), max_length=100,
        help_text=_('Ex : Directeur de clinique, Médecin généraliste'),
    )
    company = models.CharField(_('Entreprise'), max_length=100, blank=True)
    content = models.TextField(_('Témoignage'))
    photo = models.ImageField(
        _('Photo'), upload_to='testimonials/', blank=True, null=True,
    )
    photo_alt = models.CharField(_('Texte alternatif photo'), max_length=150, blank=True)
    is_active = models.BooleanField(_('Actif'), default=True)
    ordering = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('Témoignage')
        verbose_name_plural = _('Témoignages')

    def __str__(self):
        return f'{self.client_name} — {self.company}'


class Showroom(models.Model):
    """Matterport 3D/360 virtual tour embed, manageable from the admin."""
    title = models.CharField(_('Titre'), max_length=200)
    slug = models.SlugField(_('Slug'), unique=True)
    description = models.TextField(_('Description'), blank=True)
    matterport_embed_url = models.URLField(
        _('URL Matterport Showcase'),
        blank=True,
        help_text=_('URL complète, ex : https://my.matterport.com/show/?m=SPACE_ID'),
    )
    panorama_image = models.ImageField(
        _('Image panoramique 360°'), upload_to='showrooms/', blank=True, null=True,
        help_text=_('Image équirectangulaire pour la visite virtuelle 360°. Prioritaire sur l\'URL Matterport.'),
    )
    cover_image = models.ImageField(
        _('Image de couverture'), upload_to='showrooms/', blank=True, null=True,
    )
    cover_image_alt = models.CharField(
        _('Texte alternatif image'), max_length=150, blank=True,
    )
    is_featured = models.BooleanField(
        _('Afficher en page d\'accueil'), default=False,
        help_text=_('Mettre en avant sur la page d\'accueil'),
    )
    is_active = models.BooleanField(_('Actif'), default=True)
    ordering = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('Showroom virtuel')
        verbose_name_plural = _('Showrooms virtuels')

    def __str__(self):
        return self.title


class Partner(models.Model):
    """Reference / partner shown in the home page carousel. Managed from admin."""
    name = models.CharField(_('Nom'), max_length=200)
    logo = models.ImageField(
        _('Logo'), upload_to='partners/', blank=True, null=True,
        help_text=_('Logo du partenaire (optionnel). Laissez vide pour afficher uniquement le nom.'),
    )
    website_url = models.URLField(_('Site web'), blank=True)
    is_active = models.BooleanField(_('Actif'), default=True)
    ordering = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('Référence / Partenaire')
        verbose_name_plural = _('Références / Partenaires')

    def __str__(self):
        return self.name


class ShowroomGalleryImage(models.Model):
    """
    Gallery image to be shown in a slider below showrooms on the services page.
    Admin can upload pictures to this slider dynamically.
    """
    title = models.CharField(_('Titre (Optionnel)'), max_length=200, blank=True)
    image = models.ImageField(_('Image'), upload_to='showroom_gallery/')
    alt_text = models.CharField(_('Texte alternatif'), max_length=150, blank=True)
    is_active = models.BooleanField(_('Actif'), default=True)
    ordering = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('Image Galerie Showroom')
        verbose_name_plural = _('Images Galerie Showroom')

    def __str__(self):
        return self.title or f"Image #{self.id}"

