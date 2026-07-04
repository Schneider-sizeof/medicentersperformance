"""Contact forms with honeypot spam protection and math captcha."""
import random
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Contact form with:
    - Honeypot field (hidden, rejected if filled)
    - Math captcha (server-side)
    """
    # Honeypot
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label='',
    )

    # Math captcha
    captcha_a = forms.IntegerField(widget=forms.HiddenInput())
    captcha_b = forms.IntegerField(widget=forms.HiddenInput())
    captcha_answer = forms.IntegerField(
        label=_('Vérification anti-spam'),
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': _('Votre réponse'),
            'autocomplete': 'off',
        }),
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Votre nom complet'),
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('votre.email@exemple.com'),
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('+212 6XX XX XX XX'),
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Objet de votre message'),
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': _('Décrivez votre besoin ou posez-nous vos questions…'),
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        self.fields['captcha_a'].initial = a
        self.fields['captcha_b'].initial = b
        self.captcha_question = f'{a} + {b} = ?'

    def clean(self):
        cleaned_data = super().clean()

        # Honeypot check
        if cleaned_data.get('website'):
            raise forms.ValidationError(_('Soumission rejetée.'))

        # Captcha validation
        a = cleaned_data.get('captcha_a', 0)
        b = cleaned_data.get('captcha_b', 0)
        answer = cleaned_data.get('captcha_answer')
        if answer != a + b:
            raise forms.ValidationError(_('La réponse au calcul anti-spam est incorrecte.'))

        return cleaned_data
