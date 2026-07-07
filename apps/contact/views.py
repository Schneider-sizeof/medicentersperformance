"""Contact views — contact form handling with professional email notifications."""
import logging
from django.shortcuts import render, redirect
from .forms import ContactForm
from apps.core.emails import send_admin_contact_notification, send_user_contact_confirmation

logger = logging.getLogger(__name__)


def contact(request):
    """Display and process the contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message_obj = form.save()

            # Send professional HTML admin notification
            send_admin_contact_notification(message_obj)

            # Send professional HTML confirmation to user
            send_user_contact_confirmation(message_obj)

            return redirect('contact:success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    """Thank-you page after successful contact form submission."""
    return render(request, 'contact/contact_success.html')
