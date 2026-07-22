from django.contrib.admin.forms import AdminAuthenticationForm
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _

class CaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    """
    Custom admin authentication form that adds a local CAPTCHA check.
    Prevents automated brute-force attacks and credential stuffing bots.
    """
    captcha = CaptchaField(
        label=_("Vérification anti-robot"),
        error_messages={
            'invalid': _("Le code de vérification est incorrect.")
        }
    )
