"""Partnership views — B2B form handling with professional email notifications."""
import logging
from django.shortcuts import render, redirect
from .forms import PartnershipForm
from apps.core.emails import send_admin_partnership_notification, send_user_partnership_confirmation

logger = logging.getLogger(__name__)


def partnership_page(request):
    """Display and process the B2B partnership form."""
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            # Send professional HTML admin notification
            send_admin_partnership_notification(inquiry)

            # Send professional HTML confirmation to user
            send_user_partnership_confirmation(inquiry)

            return redirect('partnership:success')
    else:
        form = PartnershipForm()

    return render(request, 'partnership/partnership.html', {'form': form})


def partnership_success(request):
    """Thank-you page after successful partnership form submission."""
    return render(request, 'partnership/partnership_success.html')
