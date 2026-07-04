"""
Populate Products and Services with the 18 products and 9 services.
Run: venv\Scripts\python.exe manage.py shell < populate_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
django.setup()

from apps.services.models import Product, Service

# ============================================================
# 18 PRODUCTS
# ============================================================
products_data = [
    {
        'title': 'Mobilier médical modulaire',
        'subtitle': 'Mobilier fonctionnel et ergonomique conçu pour les espaces médicaux professionnels.',
        'slug': 'mobilier-medical-modulaire',
        'ordering': 1,
    },
    {
        'title': 'Stores',
        'subtitle': 'Stores et rideaux professionnels pour contrôler la lumière et assurer l\'intimité.',
        'slug': 'stores',
        'ordering': 2,
    },
    {
        'title': 'Bureaux',
        'subtitle': 'Bureaux de consultation et postes de travail adaptés aux professionnels de santé.',
        'slug': 'bureaux',
        'ordering': 3,
    },
    {
        'title': 'Faux plafond – habillage mural',
        'subtitle': 'Solutions de faux plafonds et d\'habillage mural pour un rendu esthétique et fonctionnel.',
        'slug': 'faux-plafond-habillage-mural',
        'ordering': 4,
    },
    {
        'title': 'Vestiaires',
        'subtitle': 'Vestiaires et casiers professionnels pour le personnel médical.',
        'slug': 'vestiaires',
        'ordering': 5,
    },
    {
        'title': 'Comptoir d\'accueil',
        'subtitle': 'Comptoirs d\'accueil sur mesure pour une première impression professionnelle.',
        'slug': 'comptoir-accueil',
        'ordering': 6,
    },
    {
        'title': 'Portes & cloisons',
        'subtitle': 'Portes techniques et cloisons modulaires pour structurer vos espaces.',
        'slug': 'portes-cloisons',
        'ordering': 7,
    },
    {
        'title': 'Chaises & canapés',
        'subtitle': 'Mobilier d\'assise confortable pour salles d\'attente et espaces de consultation.',
        'slug': 'chaises-canapes',
        'ordering': 8,
    },
    {
        'title': 'Kitchenette',
        'subtitle': 'Kitchenettes compactes et fonctionnelles pour les espaces de pause du personnel.',
        'slug': 'kitchenette',
        'ordering': 9,
    },
    {
        'title': 'Éclairage & sonorisation',
        'subtitle': 'Systèmes d\'éclairage professionnel et solutions de sonorisation pour vos locaux.',
        'slug': 'eclairage-sonorisation',
        'ordering': 10,
    },
    {
        'title': 'SSI',
        'subtitle': 'Systèmes de sécurité incendie conformes aux normes en vigueur.',
        'slug': 'ssi',
        'ordering': 11,
    },
    {
        'title': 'Mesure de sécurité et de contrôle',
        'subtitle': 'Équipements de vidéosurveillance, contrôle d\'accès et alarmes.',
        'slug': 'mesure-securite-controle',
        'ordering': 12,
    },
    {
        'title': 'Climatisation',
        'subtitle': 'Solutions de climatisation et traitement d\'air adaptées aux environnements médicaux.',
        'slug': 'climatisation',
        'ordering': 13,
    },
    {
        'title': 'Blouses / tuniques / vêtements médicaux',
        'subtitle': 'Tenues professionnelles personnalisées pour le personnel médical et paramédical.',
        'slug': 'blouses-tuniques-vetements-medicaux',
        'ordering': 14,
    },
    {
        'title': 'Accessoires & gadgets décoratifs',
        'subtitle': 'Éléments décoratifs et accessoires pour personnaliser vos espaces.',
        'slug': 'accessoires-gadgets-decoratifs',
        'ordering': 15,
    },
    {
        'title': 'Logiciel de gestion',
        'subtitle': 'Solutions logicielles de gestion pour cabinets et cliniques.',
        'slug': 'logiciel-gestion',
        'ordering': 16,
    },
    {
        'title': 'Enseignes publicitaires',
        'subtitle': 'Enseignes lumineuses et panneaux publicitaires extérieurs sur mesure.',
        'slug': 'enseignes-publicitaires',
        'ordering': 17,
    },
    {
        'title': 'Signalétique & enseigne d\'intérieur',
        'subtitle': 'Signalétique intérieure professionnelle pour orienter patients et visiteurs.',
        'slug': 'signaletique-enseigne-interieur',
        'ordering': 18,
    },
]

# ============================================================
# 9 SERVICES
# ============================================================
services_data = [
    {
        'title': 'Architecture d\'intérieur',
        'subtitle': 'Conception et réalisation d\'espaces médicaux fonctionnels et esthétiques.',
        'slug': 'architecture-interieur',
        'icon_class': 'bi-building',
        'short_description': 'Conception et réalisation d\'espaces médicaux fonctionnels et esthétiques.',
        'long_description': '<p>Notre équipe d\'architectes d\'intérieur conçoit des espaces médicaux qui allient fonctionnalité, confort et esthétique. Nous prenons en charge la conception complète de votre espace, de l\'étude initiale à la réalisation finale.</p>',
        'ordering': 1,
    },
    {
        'title': 'Aménagement espace enfant',
        'subtitle': 'Espaces ludiques et sécurisés pour accueillir les jeunes patients.',
        'slug': 'amenagement-espace-enfant',
        'icon_class': 'bi-emoji-smile',
        'short_description': 'Espaces ludiques et sécurisés pour accueillir les jeunes patients.',
        'long_description': '<p>Nous concevons des espaces enfants chaleureux et ludiques au sein de vos locaux médicaux. Mobilier adapté, couleurs vives, éléments interactifs — tout est pensé pour rassurer les jeunes patients et faciliter leur expérience.</p>',
        'ordering': 2,
    },
    {
        'title': 'Aménagement PMR',
        'subtitle': 'Mise en conformité et aménagement pour personnes à mobilité réduite.',
        'slug': 'amenagement-pmr',
        'icon_class': 'bi-universal-access',
        'short_description': 'Mise en conformité et aménagement pour personnes à mobilité réduite.',
        'long_description': '<p>Nous garantissons l\'accessibilité de vos espaces médicaux pour les personnes à mobilité réduite. Rampes, sanitaires adaptés, signalétique tactile, mobilier ajustable — nos solutions respectent les normes en vigueur.</p>',
        'ordering': 3,
    },
    {
        'title': 'Marketing médical',
        'subtitle': 'Stratégies marketing digitales et traditionnelles pour le secteur médical.',
        'slug': 'marketing-medical',
        'icon_class': 'bi-megaphone',
        'short_description': 'Stratégies marketing digitales et traditionnelles pour le secteur médical.',
        'long_description': '<p>Nous développons des stratégies marketing sur mesure pour les professionnels de santé. Référencement, publicité, gestion des avis patients, campagnes ciblées — nous vous aidons à développer votre visibilité.</p>',
        'ordering': 4,
    },
    {
        'title': 'Charte graphique',
        'subtitle': 'Création d\'identité visuelle professionnelle pour votre établissement.',
        'slug': 'charte-graphique',
        'icon_class': 'bi-palette',
        'short_description': 'Création d\'identité visuelle professionnelle pour votre établissement.',
        'long_description': '<p>Nous créons une identité visuelle forte et cohérente pour votre établissement de santé. Logo, typographie, palette de couleurs, papeterie — chaque élément est conçu pour refléter votre professionnalisme.</p>',
        'ordering': 5,
    },
    {
        'title': 'Conception graphique & impression',
        'subtitle': 'Design graphique et impression de supports de communication professionnels.',
        'slug': 'conception-graphique-impression',
        'icon_class': 'bi-printer',
        'short_description': 'Design graphique et impression de supports de communication professionnels.',
        'long_description': '<p>De la conception à l\'impression, nous produisons tous vos supports de communication : brochures, cartes de visite, flyers, affiches, roll-ups et bien plus.</p>',
        'ordering': 6,
    },
    {
        'title': 'Photographie corporate & display vidéo',
        'subtitle': 'Photos professionnelles et vidéos pour valoriser votre image.',
        'slug': 'photographie-corporate-display-video',
        'icon_class': 'bi-camera',
        'short_description': 'Photos professionnelles et vidéos pour valoriser votre image.',
        'long_description': '<p>Nous réalisons des reportages photos et vidéos professionnels pour valoriser votre établissement. Portraits d\'équipe, visite virtuelle, présentation de vos services — chaque contenu est conçu pour renforcer votre image.</p>',
        'ordering': 7,
    },
    {
        'title': 'Community management',
        'subtitle': 'Gestion de vos réseaux sociaux et animation de votre communauté en ligne.',
        'slug': 'community-management',
        'icon_class': 'bi-people',
        'short_description': 'Gestion de vos réseaux sociaux et animation de votre communauté en ligne.',
        'long_description': '<p>Nous prenons en charge la gestion quotidienne de vos réseaux sociaux. Création de contenu, planification éditoriale, interaction avec votre audience — nous développons votre présence en ligne.</p>',
        'ordering': 8,
    },
    {
        'title': 'Coaching et Formation',
        'subtitle': 'Programmes de formation et coaching pour optimiser la gestion de votre établissement.',
        'slug': 'coaching-formation',
        'icon_class': 'bi-mortarboard',
        'short_description': 'Programmes de formation et coaching pour optimiser la gestion de votre établissement.',
        'long_description': '<p>Nous proposons des programmes de formation et de coaching personnalisés pour les professionnels de santé. Management, accueil patient, marketing digital — nos formations vous aident à exceller.</p>',
        'ordering': 9,
    },
]

# Populate Products
created_products = 0
for data in products_data:
    obj, created = Product.objects.get_or_create(
        slug=data['slug'],
        defaults=data,
    )
    if created:
        created_products += 1
        print(f'  + Created product: {obj.title}')
    else:
        print(f'  = Product already exists: {obj.title}')

# Populate Services (update existing or create new)
created_services = 0
updated_services = 0
for data in services_data:
    slug = data['slug']
    obj, created = Service.objects.get_or_create(
        slug=slug,
        defaults=data,
    )
    if created:
        created_services += 1
        print(f'  + Created service: {obj.title}')
    else:
        # Update subtitle if missing
        changed = False
        if not obj.subtitle and data.get('subtitle'):
            obj.subtitle = data['subtitle']
            changed = True
        if not obj.short_description and data.get('short_description'):
            obj.short_description = data['short_description']
            changed = True
        if not obj.long_description and data.get('long_description'):
            obj.long_description = data['long_description']
            changed = True
        if not obj.icon_class and data.get('icon_class'):
            obj.icon_class = data['icon_class']
            changed = True
        if changed:
            obj.save()
            updated_services += 1
            print(f'  ~ Updated service: {obj.title}')
        else:
            print(f'  = Service already exists: {obj.title}')

print(f'\nDone! Products: {created_products} created. Services: {created_services} created, {updated_services} updated.')
