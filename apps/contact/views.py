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

            # Send notification email
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

            return redirect('contact:success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    """Thank-you page after successful contact form submission."""
    return render(request, 'contact/contact_success.html')
