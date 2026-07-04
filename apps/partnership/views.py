"""Partnership views — B2B form handling with email notification."""
import logging
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import PartnershipForm

logger = logging.getLogger(__name__)


def partnership_page(request):
    """Display and process the B2B partnership form."""
    if request.method == 'POST':
        form = PartnershipForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            # Send notification email
            try:
                send_mail(
                    subject=f'Nouvelle demande de partenariat — {inquiry.company_name}',
                    message=(
                        f'Nouvelle demande de partenariat :\n\n'
                        f'Entreprise : {inquiry.company_name}\n'
                        f'Contact : {inquiry.contact_person}\n'
                        f'Poste : {inquiry.position}\n'
                        f'Email : {inquiry.email}\n'
                        f'Téléphone : {inquiry.phone}\n'
                        f'Pays : {inquiry.country}\n'
                        f'Ville : {inquiry.city}\n'
                        f'Site web : {inquiry.company_website}\n'
                        f'Secteur : {inquiry.activity_sector}\n'
                        f'Années d\'activité : {inquiry.years_in_business}\n'
                        f'Nombre d\'employés : {inquiry.num_employees}\n\n'
                        f'Produits/Services d\'intérêt :\n{inquiry.products_of_interest}\n\n'
                        f'Message :\n{inquiry.message}\n'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.NOTIFICATION_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                logger.warning('Failed to send partnership notification: %s', e)

            return redirect('partnership:success')
    else:
        form = PartnershipForm()

    return render(request, 'partnership/partnership.html', {'form': form})


def partnership_success(request):
    """Thank-you page after successful partnership form submission."""
    return render(request, 'partnership/partnership_success.html')
