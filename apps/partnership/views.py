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

            # Send notification email to admin
            try:
                send_mail(
                    subject=f'Nouvelle demande de partenariat — {inquiry.company_name}',
                    message=(
                        f'Nouvelle demande reçue depuis le site web :\n\n'
                        f'Type de demande : {inquiry.get_partnership_type_display()}\n'
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
                logger.warning('Failed to send partnership admin notification: %s', e)

            # Send confirmation email to the user
            try:
                from django.utils.translation import get_language
                current_lang = get_language()
                
                type_display = inquiry.get_partnership_type_display()
                
                if current_lang == 'ar':
                    subject = "تأكيد طلب الشراكة — MEDICENTERS PERFORMANCE"
                    body = (
                        f"مرحباً {inquiry.contact_person}،\n\n"
                        f"نشكركم على اهتمامكم بـ MEDICENTERS PERFORMANCE.\n\n"
                        f"لقد تلقينا طلبكم بنجاح بصفتكم: {type_display}.\n"
                        f"يقوم فريقنا التجاري بدراسة طلبكم بعناية فائقة، وسنتواصل معكم في غضون 48 ساعة عمل كحد أقصى لمناقشة مشروعكم.\n\n"
                        f"مع خالص التقدير،\n"
                        f"فريق MEDICENTERS PERFORMANCE"
                    )
                elif current_lang == 'en':
                    subject = "Partnership Inquiry Confirmation — MEDICENTERS PERFORMANCE"
                    body = (
                        f"Hello {inquiry.contact_person} Corporate,\n\n"
                        f"Thank you for your interest in MEDICENTERS PERFORMANCE.\n\n"
                        f"We have successfully received your inquiry as a: {type_display}.\n"
                        f"Our business team is reviewing your request with the utmost care, and we will get back to you within 48 business hours to discuss your project.\n\n"
                        f"Best regards,\n"
                        f"The MEDICENTERS PERFORMANCE Team"
                    )
                else: # French / Default
                    subject = "Confirmation de votre demande — MEDICENTERS PERFORMANCE"
                    body = (
                        f"Bonjour {inquiry.contact_person},\n\n"
                        f"Nous vous remercions pour l'intérêt que vous portez à MEDICENTERS PERFORMANCE.\n\n"
                        f"Votre demande en tant que : {type_display} a bien été reçue.\n"
                        f"Notre équipe commerciale étudie votre demande avec le plus grand soin et vous contactera sous 48 heures ouvrées pour échanger sur votre projet.\n\n"
                        f"Cordialement,\n"
                        f"L'équipe MEDICENTERS PERFORMANCE"
                    )
                
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[inquiry.email],
                    fail_silently=True,
                )
            except Exception as e:
                logger.warning('Failed to send partnership user confirmation: %s', e)

            return redirect('partnership:success')
    else:
        form = PartnershipForm()

    return render(request, 'partnership/partnership.html', {'form': form})


def partnership_success(request):
    """Thank-you page after successful partnership form submission."""
    return render(request, 'partnership/partnership_success.html')
