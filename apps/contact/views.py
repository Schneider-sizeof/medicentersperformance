"""Contact views — contact form handling with email notification."""
import logging
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

logger = logging.getLogger(__name__)


def contact(request):
    """Display and process the contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message_obj = form.save()

            # Send notification email to admin
            try:
                send_mail(
                    subject=f'Nouveau message — {message_obj.subject}',
                    message=(
                        f'Nouveau message de contact :\n\n'
                        f'Nom : {message_obj.name}\n'
                        f'Email : {message_obj.email}\n'
                        f'Téléphone : {message_obj.phone}\n'
                        f'Sujet : {message_obj.subject}\n\n'
                        f'Message :\n{message_obj.message}\n'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.NOTIFICATION_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                logger.warning('Failed to send contact notification: %s', e)

            # Send confirmation email to the user
            try:
                from django.utils.translation import get_language
                current_lang = get_language()

                if current_lang == 'ar':
                    subject = "تأكيد رسالتكم — MEDICENTERS PERFORMANCE"
                    body = (
                        f"مرحباً {message_obj.name}،\n\n"
                        f"نشكركم على تواصلكم مع MEDICENTERS PERFORMANCE.\n\n"
                        f"لقد تلقينا رسالتكم بخصوص: {message_obj.subject}.\n"
                        f"سيقوم فريقنا بالرد عليكم في أقرب وقت ممكن.\n\n"
                        f"مع خالص التقدير،\n"
                        f"فريق MEDICENTERS PERFORMANCE"
                    )
                elif current_lang == 'en':
                    subject = "Message Confirmation — MEDICENTERS PERFORMANCE"
                    body = (
                        f"Hello {message_obj.name},\n\n"
                        f"Thank you for contacting MEDICENTERS PERFORMANCE.\n\n"
                        f"We have received your message regarding: {message_obj.subject}.\n"
                        f"Our team will get back to you as soon as possible.\n\n"
                        f"Best regards,\n"
                        f"The MEDICENTERS PERFORMANCE Team"
                    )
                else:
                    subject = "Confirmation de votre message — MEDICENTERS PERFORMANCE"
                    body = (
                        f"Bonjour {message_obj.name},\n\n"
                        f"Nous vous remercions d'avoir contacté MEDICENTERS PERFORMANCE.\n\n"
                        f"Votre message concernant : {message_obj.subject} a bien été reçu.\n"
                        f"Notre équipe vous répondra dans les plus brefs délais.\n\n"
                        f"Cordialement,\n"
                        f"L'équipe MEDICENTERS PERFORMANCE"
                    )

                send_mail(
                    subject=subject,
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[message_obj.email],
                    fail_silently=True,
                )
            except Exception as e:
                logger.warning('Failed to send contact user confirmation: %s', e)

            return redirect('contact:success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    """Thank-you page after successful contact form submission."""
    return render(request, 'contact/contact_success.html')
