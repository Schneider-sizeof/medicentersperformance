"""Partnership app models — B2B partnership/reseller inquiries."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class PartnershipInquiry(models.Model):
    """A B2B partnership or reseller inquiry submitted through the form."""
    PARTNERSHIP_TYPES = [
        ('revendeur', _('Revendeur / Distributeur')),
        ('partenaire', _('Partenaire')),
        ('investisseur', _('Investisseur')),
    ]
    partnership_type = models.CharField(
        _('Type de partenariat souhaité'),
        max_length=20,
        choices=PARTNERSHIP_TYPES,
        default='partenaire',
    )
    company_name = models.CharField(_('Nom de l\'entreprise'), max_length=200)
    contact_person = models.CharField(_('Personne de contact'), max_length=150)
    position = models.CharField(_('Poste'), max_length=100, blank=True)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Téléphone'), max_length=30)
    country = models.CharField(_('Pays'), max_length=100, blank=True)
    city = models.CharField(_('Ville'), max_length=100, blank=True)
    company_website = models.URLField(_('Site web'), blank=True)
    activity_sector = models.CharField(_('Secteur d\'activité'), max_length=200, blank=True)
    years_in_business = models.CharField(_('Années d\'activité'), max_length=20, blank=True)
    num_employees = models.CharField(_('Nombre d\'employés'), max_length=50, blank=True)
    products_of_interest = models.TextField(
        _('Produits/Services d\'intérêt'), blank=True,
        help_text=_('Quels produits ou services vous intéressent ?'),
    )
    message = models.TextField(_('Message'))
    created_at = models.DateTimeField(_('Reçu le'), auto_now_add=True)
    is_read = models.BooleanField(_('Lu'), default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Demande de partenariat')
        verbose_name_plural = _('Demandes de partenariat')

    def __str__(self):
        return f'{self.company_name} — {self.contact_person}'
