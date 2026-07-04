"""Recruitment forms with honeypot spam protection and math captcha."""
import random
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Application, JobPosting


class ApplicationForm(forms.ModelForm):
    """
    Job application form with:
    - Honeypot field (hidden, rejected if filled)
    - Math captcha (server-side, no external dependency)
    - CV file validation (.pdf/.doc/.docx, max 5 MB)
    """
    # Honeypot — hidden field, bots fill it, humans don't
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label='',
    )

    # Math captcha fields
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
        model = Application
        fields = ['full_name', 'email', 'phone', 'position', 'cv_file', 'cover_message']
        widgets = {
            'full_name': forms.TextInput(attrs={
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
            'cv_file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
            }),
            'cover_message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': _('Présentez-vous et expliquez votre motivation…'),
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Position dropdown: active job postings + spontaneous option
        self.fields['position'].queryset = JobPosting.objects.filter(is_active=True)
        self.fields['position'].empty_label = _('Candidature spontanée')
        self.fields['position'].required = False
        self.fields['position'].widget.attrs.update({'class': 'form-select'})

        # Generate random captcha numbers
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

    def clean_cv_file(self):
        """Validate CV file extension and size."""
        cv = self.cleaned_data.get('cv_file')
        if cv:
            # Extension check
            allowed_extensions = ['.pdf', '.doc', '.docx']
            ext = '.' + cv.name.rsplit('.', 1)[-1].lower() if '.' in cv.name else ''
            if ext not in allowed_extensions:
                raise forms.ValidationError(
                    _('Format non supporté. Veuillez envoyer un fichier PDF, DOC ou DOCX.')
                )
            # Size check (5 MB)
            if cv.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    _('Le fichier est trop volumineux. Taille maximale : 5 Mo.')
                )
        return cv
