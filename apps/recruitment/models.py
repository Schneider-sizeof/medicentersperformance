"""Recruitment app models — job postings and applications."""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class JobPosting(models.Model):
    """An open position, managed from the Django admin."""

    CONTRACT_TYPES = [
        ('CDI', _('CDI')),
        ('CDD', _('CDD')),
        ('Stage', _('Stage')),
        ('Freelance', _('Freelance')),
    ]

    title = models.CharField(_('Titre du poste'), max_length=200)
    slug = models.SlugField(_('Slug'), unique=True)
    department = models.CharField(_('Département'), max_length=100, blank=True)
    location = models.CharField(_('Lieu'), max_length=100, default='Tanger, Maroc')
    contract_type = models.CharField(
        _('Type de contrat'), max_length=20,
        choices=CONTRACT_TYPES, default='CDI',
    )
    description = models.TextField(_('Description du poste'))
    requirements = models.TextField(
        _('Profil recherché'),
        help_text=_('Qualifications et compétences requises'),
    )
    is_active = models.BooleanField(_('Actif'), default=True)
    posted_date = models.DateTimeField(_('Date de publication'), auto_now_add=True)

    class Meta:
        ordering = ['-posted_date']
        verbose_name = _('Offre d\'emploi')
        verbose_name_plural = _('Offres d\'emploi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{reverse('recruitment:careers')}#job-{self.pk}"


class Application(models.Model):
    """
    Job application submitted via the Recruitment form.
    Stores the CV file and sends a notification email on creation.
    """
    full_name = models.CharField(_('Nom complet'), max_length=150)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Téléphone'), max_length=20)
    position = models.ForeignKey(
        JobPosting, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='applications', verbose_name=_('Poste'),
        help_text=_('Laisser vide pour candidature spontanée'),
    )
    cv_file = models.FileField(
        _('CV (PDF, DOC, DOCX)'), upload_to='applications/cvs/',
    )
    cover_message = models.TextField(_('Message de motivation'), blank=True)
    submitted_at = models.DateTimeField(_('Soumis le'), auto_now_add=True)
    is_reviewed = models.BooleanField(_('Examiné'), default=False)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = _('Candidature')
        verbose_name_plural = _('Candidatures')

    def __str__(self):
        position_label = self.position.title if self.position else 'Candidature spontanée'
        return f'{self.full_name} — {position_label}'
