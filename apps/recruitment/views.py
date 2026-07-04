"""Recruitment views — careers page and application handling."""
import logging
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .models import JobPosting
from .forms import ApplicationForm

logger = logging.getLogger(__name__)


def careers(request):
    """Display open positions and handle job applications."""
    jobs = JobPosting.objects.filter(is_active=True)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()

            # Send notification email
            position_label = (
                application.position.title if application.position
                else 'Candidature spontanée'
            )
            try:
                send_mail(
                    subject=f'Nouvelle candidature — {position_label}',
                    message=(
                        f'Nouvelle candidature reçue :\n\n'
                        f'Nom : {application.full_name}\n'
                        f'Email : {application.email}\n'
                        f'Téléphone : {application.phone}\n'
                        f'Poste : {position_label}\n'
                        f'Message :\n{application.cover_message}\n'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.NOTIFICATION_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                logger.warning('Failed to send application notification: %s', e)

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
