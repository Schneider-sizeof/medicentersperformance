"""Contact app models — messages submitted via the contact form."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    """A message submitted through the Contact page form."""
    name = models.CharField(_('Nom'), max_length=150)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Téléphone'), max_length=20)
    subject = models.CharField(_('Sujet'), max_length=200)
    message = models.TextField(_('Message'))
    created_at = models.DateTimeField(_('Reçu le'), auto_now_add=True)
    is_read = models.BooleanField(_('Lu'), default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Message de contact')
        verbose_name_plural = _('Messages de contact')

    def __str__(self):
        return f'{self.name} — {self.subject}'
