"""Shared email utilities — professional HTML email templates for all forms."""
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import get_language
import logging

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────────────────────
# Brand colours & constants
# ──────────────────────────────────────────────────────────────────────
BRAND_MAROON = '#8B1A1A'
BRAND_DARK = '#1a1a1a'
BRAND_GREY = '#f5f5f5'
BRAND_WHITE = '#ffffff'
BRAND_TEXT = '#333333'
BRAND_MUTED = '#777777'
SITE_URL = 'https://medicentersperformance.pythonanywhere.com'
LOGO_URL = f'{SITE_URL}/static/images/logo.png'


def _base_html(body_content, direction='ltr', lang='fr'):
    """Wrap body_content in a professional responsive HTML email shell."""
    align = 'right' if direction == 'rtl' else 'left'
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MEDICENTERS PERFORMANCE</title>
</head>
<body style="margin:0;padding:0;background-color:{BRAND_GREY};font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:{BRAND_GREY};">
<tr><td align="center" style="padding:24px 16px;">

<!-- Container -->
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background-color:{BRAND_WHITE};border-radius:12px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">

<!-- Header -->
<tr>
<td style="background:linear-gradient(135deg,{BRAND_DARK} 0%,{BRAND_MAROON} 100%);padding:32px 40px;text-align:center;">
<img src="{LOGO_URL}" alt="MEDICENTERS PERFORMANCE" width="160" style="display:inline-block;max-width:160px;height:auto;" />
</td>
</tr>

<!-- Body -->
<tr>
<td style="padding:40px;text-align:{align};direction:{direction};">
{body_content}
</td>
</tr>

<!-- Footer -->
<tr>
<td style="background-color:{BRAND_GREY};padding:24px 40px;text-align:center;border-top:1px solid #e0e0e0;">
<p style="margin:0 0 8px;font-size:12px;color:{BRAND_MUTED};">
    MEDICENTERS PERFORMANCE — Aménagement médical professionnel
</p>
<p style="margin:0;font-size:12px;color:{BRAND_MUTED};">
    <a href="{SITE_URL}" style="color:{BRAND_MAROON};text-decoration:none;">medicentersperformance.com</a>
    &nbsp;|&nbsp;
    <a href="https://wa.me/212660785038" style="color:{BRAND_MAROON};text-decoration:none;">WhatsApp</a>
</p>
</td>
</tr>

</table>
</td></tr>
</table>
</body>
</html>'''


def _get_direction_and_lang():
    """Return (direction, lang_code) based on current Django language."""
    lang = get_language() or 'fr'
    direction = 'rtl' if lang == 'ar' else 'ltr'
    return direction, lang


# ──────────────────────────────────────────────────────────────────────
# Reusable HTML building blocks
# ──────────────────────────────────────────────────────────────────────

def _badge(text, color=BRAND_MAROON):
    return (
        f'<span style="display:inline-block;background:{color};color:#fff;'
        f'font-size:11px;font-weight:700;letter-spacing:.5px;padding:4px 12px;'
        f'border-radius:4px;text-transform:uppercase;">{text}</span>'
    )


def _field_row(label, value):
    if not value:
        return ''
    return (
        f'<tr>'
        f'<td style="padding:8px 12px;font-size:13px;color:{BRAND_MUTED};'
        f'font-weight:600;white-space:nowrap;vertical-align:top;border-bottom:1px solid #f0f0f0;">{label}</td>'
        f'<td style="padding:8px 12px;font-size:14px;color:{BRAND_TEXT};'
        f'border-bottom:1px solid #f0f0f0;">{value}</td>'
        f'</tr>'
    )


def _data_table(rows_html):
    return (
        f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        f'style="border:1px solid #e8e8e8;border-radius:8px;overflow:hidden;margin:16px 0;">'
        f'{rows_html}</table>'
    )


def _heading(text):
    return f'<h2 style="margin:0 0 8px;font-size:20px;color:{BRAND_DARK};font-weight:700;">{text}</h2>'


def _paragraph(text):
    return f'<p style="margin:0 0 16px;font-size:15px;line-height:1.7;color:{BRAND_TEXT};">{text}</p>'


def _separator():
    return f'<hr style="border:none;border-top:1px solid #e8e8e8;margin:24px 0;" />'


# ──────────────────────────────────────────────────────────────────────
# Send helper — sends both HTML + plain-text fallback
# ──────────────────────────────────────────────────────────────────────

def _send(subject, plain_text, html_content, to_list):
    """Send an email with HTML content and plain-text fallback."""
    try:
        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=to_list,
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send(fail_silently=True)
    except Exception as e:
        logger.warning('Email send failed: %s', e)


# ══════════════════════════════════════════════════════════════════════
#  ADMIN NOTIFICATIONS
# ══════════════════════════════════════════════════════════════════════

def send_admin_contact_notification(message_obj):
    """Admin notification for a new Contact form submission."""
    badge = _badge('FORMULAIRE CONTACT', '#2196F3')
    rows = (
        _field_row('Nom', message_obj.name)
        + _field_row('Email', f'<a href="mailto:{message_obj.email}" style="color:{BRAND_MAROON};">{message_obj.email}</a>')
        + _field_row('Téléphone', message_obj.phone)
        + _field_row('Sujet', message_obj.subject)
    )
    body = (
        f'{badge}'
        f'{_heading("Nouveau message de contact")}'
        f'{_paragraph("Un visiteur a soumis le formulaire de contact sur votre site web.")}'
        f'{_data_table(rows)}'
        f'{_separator()}'
        f'<p style="margin:0 0 4px;font-size:13px;color:{BRAND_MUTED};font-weight:600;">Message :</p>'
        f'<div style="background:{BRAND_GREY};border-radius:8px;padding:16px;font-size:14px;'
        f'line-height:1.7;color:{BRAND_TEXT};white-space:pre-wrap;">{message_obj.message}</div>'
    )
    html = _base_html(body)
    plain = (
        f'[FORMULAIRE CONTACT]\n\n'
        f'Nom : {message_obj.name}\nEmail : {message_obj.email}\n'
        f'Téléphone : {message_obj.phone}\nSujet : {message_obj.subject}\n\n'
        f'Message :\n{message_obj.message}'
    )
    _send(
        subject=f'📩 Nouveau contact — {message_obj.subject}',
        plain_text=plain, html_content=html,
        to_list=[settings.NOTIFICATION_EMAIL],
    )


def send_admin_partnership_notification(inquiry):
    """Admin notification for a new Partnership/Reseller/Investor inquiry."""
    type_display = inquiry.get_partnership_type_display()
    type_colors = {
        'revendeur': '#FF9800',
        'partenaire': '#4CAF50',
        'investisseur': '#9C27B0',
    }
    color = type_colors.get(inquiry.partnership_type, BRAND_MAROON)
    badge = _badge(f'PARTENARIAT — {type_display.upper()}', color)
    rows = (
        _field_row('Type', f'<strong>{type_display}</strong>')
        + _field_row('Entreprise', inquiry.company_name)
        + _field_row('Contact', inquiry.contact_person)
        + _field_row('Poste', inquiry.position)
        + _field_row('Email', f'<a href="mailto:{inquiry.email}" style="color:{BRAND_MAROON};">{inquiry.email}</a>')
        + _field_row('Téléphone', inquiry.phone)
        + _field_row('Pays', inquiry.country)
        + _field_row('Ville', inquiry.city)
        + _field_row('Site web', f'<a href="{inquiry.company_website}" style="color:{BRAND_MAROON};">{inquiry.company_website}</a>' if inquiry.company_website else '')
        + _field_row('Secteur', inquiry.activity_sector)
        + _field_row("Années d'activité", inquiry.years_in_business)
        + _field_row("Nombre d'employés", inquiry.num_employees)
    )
    body = (
        f'{badge}'
        f'{_heading("Nouvelle demande de partenariat")}'
        f'{_paragraph(f"Une nouvelle demande <strong>{type_display}</strong> a été soumise depuis votre site web.")}'
        f'{_data_table(rows)}'
    )
    if inquiry.products_of_interest:
        body += (
            f'{_separator()}'
            f'<p style="margin:0 0 4px;font-size:13px;color:{BRAND_MUTED};font-weight:600;">Produits / Services d\'intérêt :</p>'
            f'<div style="background:{BRAND_GREY};border-radius:8px;padding:16px;font-size:14px;'
            f'line-height:1.7;color:{BRAND_TEXT};white-space:pre-wrap;">{inquiry.products_of_interest}</div>'
        )
    body += (
        f'{_separator()}'
        f'<p style="margin:0 0 4px;font-size:13px;color:{BRAND_MUTED};font-weight:600;">Message :</p>'
        f'<div style="background:{BRAND_GREY};border-radius:8px;padding:16px;font-size:14px;'
        f'line-height:1.7;color:{BRAND_TEXT};white-space:pre-wrap;">{inquiry.message}</div>'
    )
    html = _base_html(body)
    plain = (
        f'[PARTENARIAT — {type_display.upper()}]\n\n'
        f'Type : {type_display}\nEntreprise : {inquiry.company_name}\n'
        f'Contact : {inquiry.contact_person}\nEmail : {inquiry.email}\n'
        f'Téléphone : {inquiry.phone}\n\nMessage :\n{inquiry.message}'
    )
    _send(
        subject=f'🤝 Nouveau {type_display} — {inquiry.company_name}',
        plain_text=plain, html_content=html,
        to_list=[settings.NOTIFICATION_EMAIL],
    )


def send_admin_recruitment_notification(application):
    """Admin notification for a new job application."""
    position_label = (
        application.position.title if application.position
        else 'Candidature spontanée'
    )
    badge = _badge('RECRUTEMENT', '#E91E63')
    rows = (
        _field_row('Nom complet', application.full_name)
        + _field_row('Email', f'<a href="mailto:{application.email}" style="color:{BRAND_MAROON};">{application.email}</a>')
        + _field_row('Téléphone', application.phone)
        + _field_row('Poste', position_label)
    )
    body = (
        f'{badge}'
        f'{_heading("Nouvelle candidature")}'
        f'{_paragraph(f"Un candidat a postulé pour le poste : <strong>{position_label}</strong>.")}'
        f'{_data_table(rows)}'
        f'{_separator()}'
        f'<p style="margin:0 0 4px;font-size:13px;color:{BRAND_MUTED};font-weight:600;">Message de motivation :</p>'
        f'<div style="background:{BRAND_GREY};border-radius:8px;padding:16px;font-size:14px;'
        f'line-height:1.7;color:{BRAND_TEXT};white-space:pre-wrap;">{application.cover_message}</div>'
    )
    if application.cv:
        body += (
            f'<p style="margin:16px 0 0;font-size:13px;color:{BRAND_MUTED};">'
            f'📎 CV joint : <a href="{SITE_URL}{application.cv.url}" style="color:{BRAND_MAROON};">'
            f'{application.cv.name}</a></p>'
        )
    html = _base_html(body)
    plain = (
        f'[RECRUTEMENT]\n\nNom : {application.full_name}\n'
        f'Email : {application.email}\nTéléphone : {application.phone}\n'
        f'Poste : {position_label}\n\nMessage :\n{application.cover_message}'
    )
    _send(
        subject=f'👤 Nouvelle candidature — {position_label}',
        plain_text=plain, html_content=html,
        to_list=[settings.NOTIFICATION_EMAIL],
    )


# ══════════════════════════════════════════════════════════════════════
#  USER CONFIRMATIONS
# ══════════════════════════════════════════════════════════════════════

def _user_confirmation_body(greeting, intro, detail_label, detail_value, response_time, closing, sign_off):
    """Build the inner HTML for a user confirmation email."""
    return (
        f'{_heading(greeting)}'
        f'{_paragraph(intro)}'
        f'<div style="background:{BRAND_GREY};border-left:4px solid {BRAND_MAROON};'
        f'border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0;">'
        f'<p style="margin:0;font-size:13px;color:{BRAND_MUTED};font-weight:600;">{detail_label}</p>'
        f'<p style="margin:4px 0 0;font-size:15px;color:{BRAND_DARK};font-weight:600;">{detail_value}</p>'
        f'</div>'
        f'{_paragraph(response_time)}'
        f'{_separator()}'
        f'<p style="margin:0 0 4px;font-size:14px;color:{BRAND_TEXT};">{closing}</p>'
        f'<p style="margin:0;font-size:14px;color:{BRAND_DARK};font-weight:700;">{sign_off}</p>'
    )


def send_user_contact_confirmation(message_obj):
    """Send confirmation email to the user who submitted the contact form."""
    direction, lang = _get_direction_and_lang()

    if lang == 'ar':
        subject = 'تأكيد رسالتكم — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'مرحباً {message_obj.name}،',
            intro='نشكركم على تواصلكم مع <strong>MEDICENTERS PERFORMANCE</strong>. لقد تلقينا رسالتكم بنجاح.',
            detail_label='موضوع الرسالة',
            detail_value=message_obj.subject,
            response_time='سيقوم فريقنا بمعالجة طلبكم والرد عليكم في أقرب وقت ممكن، في مدة لا تتجاوز <strong>48 ساعة عمل</strong>.',
            closing='مع خالص التقدير،',
            sign_off='فريق MEDICENTERS PERFORMANCE',
        )
    elif lang == 'en':
        subject = 'Message Confirmation — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'Hello {message_obj.name},',
            intro='Thank you for contacting <strong>MEDICENTERS PERFORMANCE</strong>. We have successfully received your message.',
            detail_label='Message subject',
            detail_value=message_obj.subject,
            response_time='Our team will process your request and get back to you as soon as possible, within <strong>48 business hours</strong>.',
            closing='Best regards,',
            sign_off='The MEDICENTERS PERFORMANCE Team',
        )
    else:
        subject = 'Confirmation de votre message — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'Bonjour {message_obj.name},',
            intro='Nous vous remercions d\'avoir contacté <strong>MEDICENTERS PERFORMANCE</strong>. Votre message a bien été reçu.',
            detail_label='Sujet du message',
            detail_value=message_obj.subject,
            response_time='Notre équipe traitera votre demande et vous répondra dans les plus brefs délais, sous <strong>48 heures ouvrées</strong> maximum.',
            closing='Cordialement,',
            sign_off="L'équipe MEDICENTERS PERFORMANCE",
        )

    html = _base_html(body, direction, lang)
    plain = f'{subject}\n\n{message_obj.subject}\n'
    _send(subject=subject, plain_text=plain, html_content=html, to_list=[message_obj.email])


def send_user_partnership_confirmation(inquiry):
    """Send confirmation email to the user who submitted the partnership form."""
    direction, lang = _get_direction_and_lang()
    type_display = inquiry.get_partnership_type_display()

    if lang == 'ar':
        subject = 'تأكيد طلب الشراكة — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'مرحباً {inquiry.contact_person}،',
            intro=f'نشكركم على اهتمامكم بـ <strong>MEDICENTERS PERFORMANCE</strong>. لقد تلقينا طلبكم بنجاح.',
            detail_label='نوع الطلب',
            detail_value=type_display,
            response_time='يقوم فريقنا التجاري بدراسة طلبكم بعناية فائقة، وسنتواصل معكم في غضون <strong>48 ساعة عمل</strong> كحد أقصى لمناقشة مشروعكم.',
            closing='مع خالص التقدير،',
            sign_off='فريق MEDICENTERS PERFORMANCE',
        )
    elif lang == 'en':
        subject = 'Partnership Inquiry Confirmation — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'Hello {inquiry.contact_person},',
            intro=f'Thank you for your interest in <strong>MEDICENTERS PERFORMANCE</strong>. We have successfully received your inquiry.',
            detail_label='Inquiry type',
            detail_value=type_display,
            response_time='Our business team is reviewing your request with the utmost care and will get back to you within <strong>48 business hours</strong> to discuss your project.',
            closing='Best regards,',
            sign_off='The MEDICENTERS PERFORMANCE Team',
        )
    else:
        subject = 'Confirmation de votre demande — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'Bonjour {inquiry.contact_person},',
            intro=f'Nous vous remercions pour l\'intérêt que vous portez à <strong>MEDICENTERS PERFORMANCE</strong>. Votre demande a bien été reçue.',
            detail_label='Type de demande',
            detail_value=type_display,
            response_time='Notre équipe commerciale étudie votre demande avec le plus grand soin et vous contactera sous <strong>48 heures ouvrées</strong> pour échanger sur votre projet.',
            closing='Cordialement,',
            sign_off="L'équipe MEDICENTERS PERFORMANCE",
        )

    html = _base_html(body, direction, lang)
    plain = f'{subject}\n\n{type_display}\n'
    _send(subject=subject, plain_text=plain, html_content=html, to_list=[inquiry.email])


def send_user_recruitment_confirmation(application):
    """Send confirmation email to the user who submitted a job application."""
    direction, lang = _get_direction_and_lang()
    position_label = (
        application.position.title if application.position
        else ('Candidature spontanée' if lang == 'fr' else 'Spontaneous Application' if lang == 'en' else 'ترشح تلقائي')
    )

    if lang == 'ar':
        subject = 'تأكيد طلب التوظيف — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'مرحباً {application.full_name}،',
            intro='نشكركم على ترشحكم للعمل مع <strong>MEDICENTERS PERFORMANCE</strong>. لقد تلقينا طلبكم بنجاح.',
            detail_label='المنصب المطلوب',
            detail_value=position_label,
            response_time='يقوم فريقنا بدراسة ملفكم بعناية. سنتواصل معكم إذا كان ملفكم مطابقاً لاحتياجاتنا.',
            closing='مع خالص التقدير،',
            sign_off='فريق MEDICENTERS PERFORMANCE',
        )
    elif lang == 'en':
        subject = 'Application Confirmation — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'Hello {application.full_name},',
            intro='Thank you for applying to <strong>MEDICENTERS PERFORMANCE</strong>. We have successfully received your application.',
            detail_label='Position applied for',
            detail_value=position_label,
            response_time='Our team is carefully reviewing your profile. We will contact you if your application matches our needs.',
            closing='Best regards,',
            sign_off='The MEDICENTERS PERFORMANCE Team',
        )
    else:
        subject = 'Confirmation de votre candidature — MEDICENTERS PERFORMANCE'
        body = _user_confirmation_body(
            greeting=f'Bonjour {application.full_name},',
            intro='Nous vous remercions d\'avoir postulé chez <strong>MEDICENTERS PERFORMANCE</strong>. Votre candidature a bien été enregistrée.',
            detail_label='Poste visé',
            detail_value=position_label,
            response_time='Notre équipe étudie attentivement votre profil. Nous vous contacterons si votre candidature correspond à nos besoins.',
            closing='Cordialement,',
            sign_off="L'équipe MEDICENTERS PERFORMANCE",
        )

    html = _base_html(body, direction, lang)
    plain = f'{subject}\n\n{position_label}\n'
    _send(subject=subject, plain_text=plain, html_content=html, to_list=[application.email])
