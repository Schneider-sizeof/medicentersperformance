"""Recruitment views — careers page and application handling with professional email notifications."""
import logging
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .models import JobPosting
from .forms import ApplicationForm
from apps.core.emails import send_admin_recruitment_notification, send_user_recruitment_confirmation

logger = logging.getLogger(__name__)


def careers(request):
    """Display open positions and handle job applications."""
    jobs = JobPosting.objects.filter(is_active=True)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()

            # Send professional HTML admin notification
            send_admin_recruitment_notification(application)

            # Send professional HTML confirmation to user
            send_user_recruitment_confirmation(application)

            return redirect('recruitment:success')
    else:
        form = ApplicationForm()

    return render(request, 'recruitment/careers.html', {
        'form': form,
        'jobs': jobs,
    })


def application_success(request):
    """Thank-you page after successful application submission."""
    return render(request, 'recruitment/application_success.html')
