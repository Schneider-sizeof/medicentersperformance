"""Partnership forms with honeypot spam protection and math captcha."""
import random
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import PartnershipInquiry


class PartnershipForm(forms.ModelForm):
    """
    B2B Partnership form with:
    - Honeypot field (hidden, rejected if filled)
    - Math captcha (server-side)
    """
    # Honeypot
    website_url = forms.CharField(
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
        model = PartnershipInquiry
        fields = [
            'company_name', 'contact_person', 'position', 'email', 'phone',
            'country', 'city', 'company_website', 'activity_sector',
            'years_in_business', 'num_employees', 'products_of_interest', 'message',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Nom de votre entreprise'),
            }),
            'contact_person': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Nom complet'),
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ex : Directeur commercial'),
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('votre.email@entreprise.com'),
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('+212 6XX XX XX XX'),
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Maroc'),
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Tanger'),
            }),
            'company_website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': _('https://www.exemple.com'),
            }),
            'activity_sector': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ex : Fournitures médicales'),
            }),
            'years_in_business': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ex : 5 ans'),
            }),
            'num_employees': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ex : 10-50'),
            }),
            'products_of_interest': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': _('Quels produits ou services vous intéressent ?'),
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': _('Décrivez votre projet de partenariat ou de revente…'),
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
        if cleaned_data.get('website_url'):
            raise forms.ValidationError(_('Soumission rejetée.'))

        # Captcha validation
        a = cleaned_data.get('captcha_a', 0)
        b = cleaned_data.get('captcha_b', 0)
        answer = cleaned_data.get('captcha_answer')
        if answer != a + b:
            raise forms.ValidationError(_('La réponse au calcul anti-spam est incorrecte.'))

        return cleaned_data
