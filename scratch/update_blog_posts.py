import os
import json
import django
import datetime
from django.utils import timezone

# Setup Django Environment
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
sys.path.append(os.getcwd())
django.setup()

from apps.blog.models import BlogPost, Category

# Ensure category 1 exists in the database
category, _ = Category.objects.get_or_create(
    id=1,
    defaults={
        'name': 'Aménagement Médical',
        'name_fr': 'Aménagement Médical',
        'name_en': 'Medical Layout',
        'name_ar': 'التجهيز الطبي',
        'slug': 'amenagement-medical'
    }
)

# New Articles Data
new_posts = [
    {
        "id": 1,
        "title": "Aménagement de Cabinet Médical à Tanger : Le Guide Complet",
        "title_fr": "Aménagement de Cabinet Médical à Tanger : Le Guide Complet",
        "title_en": "Medical Office Design in Tangier: The Complete Guide",
        "title_ar": "تجهيز العيادات الطبية في طنجة: دليل كامل لتصميم مثالي",
        "slug": "amenagement-cabinet-medical-tanger",
        "excerpt": "Découvrez les clés d'un aménagement de cabinet médical réussi à Tanger : optimisation de l'espace, flux patients, confidentialité et choix de design d'intérieur médical adaptés au Maroc.",
        "excerpt_fr": "Découvrez les clés d'un aménagement de cabinet médical réussi à Tanger : optimisation de l'espace, flux patients, confidentialité et choix de design d'intérieur médical adaptés au Maroc.",
        "excerpt_en": "Discover the keys to a successful medical office design in Tangier: space optimization, patient flow, privacy, and medical interior design choices adapted to Morocco.",
        "excerpt_ar": "اكتشف مفاتيح تجهيز عيادة طبية ناجحة في طنجة: تحسين المساحة، واستقبال المرضى، ومعايير الخصوصية، وخيارات التصميم الداخلي الطبي الملائمة للمغرب.",
        "content": """<h2>L'importance de l'agencement dans un cabinet médical moderne</h2>
<p>L'<strong>aménagement d'un cabinet médical</strong> ne se limite pas à placer un bureau et une table d'examen. À Tanger et partout au Maroc, les professionnels de santé cherchent de plus en plus à optimiser leurs espaces pour offrir une expérience patient d'exception tout en garantissant un cadre de travail ergonomique et serein.</p>

<h2>1. Optimisation des flux et de la salle d'attente du médecin</h2>
<p>Le parcours du patient doit être fluide de son entrée à sa sortie. La <strong>salle d'attente d'un médecin</strong> doit inspirer le calme et la sérénité. L'utilisation de couleurs douces, d'un éclairage indirect chaleureux et de sièges ergonomiques permet de réduire l'anxiété pré-consultation. Il est également recommandé de séparer visuellement la zone d'accueil de la zone d'attente pour préserver la confidentialité.</p>

<h2>2. Le design d'intérieur médical au service de la confiance</h2>
<p>Un <strong>design d'intérieur médical</strong> professionnel renforce la crédibilité du praticien. Le choix de matériaux nobles, lavables et durables est essentiel. L'intégration de cloisons acoustiques permet de garantir la confidentialité absolue des échanges entre le médecin et son patient, un critère de choix pour les patients marocains.</p>

<h2>3. Pourquoi faire appel à un spécialiste à Tanger ?</h2>
<p>Faire appel à un expert local de l'<strong>agencement de cabinet médical à Tanger</strong> comme MEDICENTERS PERFORMANCE vous assure le respect strict des normes de sécurité et d'hygiène, tout en personnalisant votre espace selon votre spécialité médicale (généraliste, dentiste, pédiatre ou cardiologue).</p>""",
        "content_fr": """<h2>L'importance de l'agencement dans un cabinet médical moderne</h2>
<p>L'<strong>aménagement d'un cabinet médical</strong> ne se limite pas à placer un bureau et une table d'examen. À Tanger et partout au Maroc, les professionnels de santé cherchent de plus en plus à optimiser leurs espaces pour offrir une expérience patient d'exception tout en garantissant un cadre de travail ergonomique et serein.</p>

<h2>1. Optimisation des flux et de la salle d'attente du médecin</h2>
<p>Le parcours du patient doit être fluide de son entrée à sa sortie. La <strong>salle d'attente d'un médecin</strong> doit inspirer le calme et la sérénité. L'utilisation de couleurs douces, d'un éclairage indirect chaleureux et de sièges ergonomiques permet de réduire l'anxiété pré-consultation. Il est également recommandé de séparer visuellement la zone d'accueil de la zone d'attente pour préserver la confidentialité.</p>

<h2>2. Le design d'intérieur médical au service de la confiance</h2>
<p>Un <strong>design d'intérieur médical</strong> professionnel renforce la crédibilité du praticien. Le choix de matériaux nobles, lavables et durables est essentiel. L'intégration de cloisons acoustiques permet de garantir la confidentialité absolue des échanges entre le médecin et son patient, un critère de choix pour les patients marocains.</p>

<h2>3. Pourquoi faire appel à un spécialiste à Tanger ?</h2>
<p>Faire appel à un expert local de l'<strong>agencement de cabinet médical à Tanger</strong> comme MEDICENTERS PERFORMANCE vous assure le respect strict des normes de sécurité et d'hygiène, tout en personnalisant votre espace selon votre spécialité médicale (généraliste, dentiste, pédiatre ou cardiologue).</p>""",
        "content_en": """<h2>The Importance of Layout in a Modern Medical Office</h2>
<p>The <strong>design of a medical office</strong> goes far beyond placing a desk and an exam table. In Tangier and throughout Morocco, healthcare professionals are increasingly looking to optimize their spaces to provide an exceptional patient experience while ensuring an ergonomic and peaceful working environment.</p>

<h2>1. Flow Optimization and Doctor's Waiting Room</h2>
<p>The patient journey must be fluid from entry to exit. A <strong>doctor's waiting room</strong> should inspire calm and serenity. Using soft colors, warm indirect lighting, and ergonomic seating helps reduce pre-consultation anxiety. It is also recommended to visually separate the reception area from the waiting area to preserve privacy.</p>

<h2>2. Medical Interior Design Building Trust</h2>
<p>A professional <strong>medical interior design</strong> enhances the practitioner's credibility. The choice of premium, washable, and durable materials is essential. The integration of acoustic partitions guarantees the absolute confidentiality of discussions between the doctor and the patient, which is a key priority for Moroccan patients.</p>

<h2>3. Why Work with a Specialist in Tangier?</h2>
<p>Working with a local expert in <strong>medical office design in Tangier</strong> like MEDICENTERS PERFORMANCE ensures strict compliance with safety and hygiene standards, while customizing your space according to your medical specialty (general practitioner, dentist, pediatrician, or cardiologist).</p>""",
        "content_ar": """<h2>أهمية تصميم وتجهيز العيادات الطبية الحديثة</h2>
<p>لا يقتصر <strong>تجهيز العيادة الطبية</strong> على وضع مكتب وسرير فحص فقط. في طنجة والمغرب، يسعى مهنيو الصحة بشكل متزايد إلى تحسين مساحاتهم لتقديم تجربة استثنائية للمرضى مع ضمان بيئة عمل مريحة وهادئة.</p>

<h2>1. تحسين مسار المريض وغرفة انتظار الطبيب</h2>
<p>يجب أن يكون مسار المريض سلسًا من الدخول إلى الخروج. ينبغي أن توحي <strong>غرفة انتظار الطبيب</strong> بالهدوء والسكينة. يساعد استخدام الألوان الهادئة، والإضاءة غير المباشرة الدافئة، والمقاعد المريحة في تقليل التوتر قبل الاستشارة. كما يُنصح بفصل منطقة الاستقبال بصريًا عن منطقة الانتظار للحفاظ على الخصوصية.</p>

<h2>2. التصميم الداخلي الطبي في خدمة بناء الثقة</h2>
<p>يعزز <strong>التصميم الداخلي الطبي</strong> الاحترافي مصداقية الطبيب. اختيار مواد نبيلة وقابلة للغسل ومتينة أمر أساسي. كما يضمن دمج الحواجز الصوتية الخصوصية المطلقة للمحادثات بين الطبيب ومريضه، وهو معيار أساسي للمرضى في المغرب.</p>

<h2>3. لماذا تستعين بمتخصص في تجهيز العيادات بطنجة؟</h2>
<p>تضمن لك الاستعانة بخبير محلي في <strong>تجهيز العيادات الطبية بطنجة</strong> مثل MEDICENTERS PERFORMANCE الاحترام الصارم لمعايير السلامة والنظافة، مع إضفاء طابع شخصي على مساحتك وفقًا لتخصصك الطبي (طب عام، طب أسنان، طب الأطفال أو طب القلب).</p>""",
        "meta_description": "Guide d'aménagement de cabinet médical à Tanger. Découvrez comment optimiser l'espace, aménager la salle d'attente et concevoir un design adapté.",
        "meta_description_fr": "Guide d'aménagement de cabinet médical à Tanger. Découvrez comment optimiser l'espace, aménager la salle d'attente et concevoir un design adapté.",
        "meta_description_en": "Medical office design guide in Tangier. Learn how to optimize space, set up the waiting room, and create an adapted interior design.",
        "meta_description_ar": "دليل تجهيز العيادات الطبية في طنجة. اكتشف كيفية تحسين المساحة، وتهيئة غرفة الانتظار وتصميم الديكور الداخلي المناسب.",
        "featured_image_alt": "Cabinet médical moderne aménagé à Tanger",
        "featured_image_alt_fr": "Cabinet médical moderne aménagé à Tanger",
        "featured_image_alt_en": "Modern medical office designed in Tangier",
        "featured_image_alt_ar": "عيادة طبية حديثة مجهزة في طنجة",
        "author": "MEDICENTERS PERFORMANCE",
        "category_id": 1,
        "is_published": True,
        "published_date": datetime.datetime(2026, 6, 1, 9, 0, tzinfo=datetime.timezone.utc),
        "created_at": datetime.datetime(2026, 6, 1, 9, 0, tzinfo=datetime.timezone.utc),
        "updated_at": datetime.datetime(2026, 6, 1, 9, 0, tzinfo=datetime.timezone.utc),
    },
    {
        "id": 2,
        "title": "Aménagement d'Espaces Médicaux et Normes PMR au Maroc",
        "title_fr": "Aménagement d'Espaces Médicaux et Normes PMR au Maroc",
        "title_en": "Medical Space Layout and PMR Accessibility Standards in Morocco",
        "title_ar": "تجهيز المساحات الطبية ومعايير الولوجيات (PMR) في المغرب",
        "slug": "amenagement-espaces-medicaux-normes-pmr",
        "excerpt": "Aménager un espace médical conforme aux normes PMR (Personnes à Mobilité Réduite) au Maroc est une obligation légale et morale. Découvrez les dimensions et règles clés.",
        "excerpt_fr": "Aménager un espace médical conforme aux normes PMR (Personnes à Mobilité Réduite) au Maroc est une obligation légale et morale. Découvrez les dimensions et règles clés.",
        "excerpt_en": "Designing a medical space compliant with PMR (Persons with Reduced Mobility) standards in Morocco is a legal and moral obligation. Discover the key dimensions and rules.",
        "excerpt_ar": "يعد تجهيز المساحات الطبية لتتوافق مع معايير الولوجيات (ذوي الاحتياجات الخاصة) في المغرب التزامًا قانونيًا وأخلاقيًا. اكتشف الأبعاد والقواعد الأساسية.",
        "content": """<h2>L'accessibilité, un pilier de l'aménagement des espaces médicaux</h2>
<p>L'<strong>aménagement d'espaces médicaux</strong> modernes doit inclure dès sa conception l'accessibilité universelle. Au Maroc, la réglementation impose aux établissements recevant du public (ERP), y compris les cabinets et cliniques, de garantir l'accès sans encombre aux personnes à mobilité réduite (PMR).</p>

<h2>1. Les dimensions clés pour un cabinet médical conforme</h2>
<p>Pour obtenir l'autorisation d'ouverture et garantir le confort de tous, plusieurs règles de base doivent être respectées lors de l'<strong>aménagement clinique à Tanger</strong> :</p>
<ul>
    <li><strong>Les portes :</strong> Une largeur minimale de 90 cm pour permettre le passage aisé des fauteuils roulants.</li>
    <li><strong>Les couloirs :</strong> Un espace de circulation d'au moins 1,20 m à 1,40 m de large.</li>
    <li><strong>Les rampes d'accès :</strong> Une pente douce (inférieure à 5% ou 8% selon la longueur) avec mains courantes adaptées.</li>
</ul>

<h2>2. Sanitaires et mobilier adaptés aux normes PMR au Maroc</h2>
<p>L'<strong>accessibilité de votre cabinet médical</strong> s'étend également aux toilettes et au mobilier d'accueil. Les sanitaires doivent disposer d'un espace de rotation d'au moins 1,50 m de diamètre et de barres d'appui installées de façon sécurisée. Le comptoir d'accueil doit comporter une partie abaissée pour le service des patients en fauteuil roulant.</p>

<h2>3. Allier conformité réglementaire et esthétique</h2>
<p>Le respect de la <strong>réglementation sanitaire au Maroc</strong> n'exclut pas le design. Chez MEDICENTERS PERFORMANCE, nous concevons des rampes d'accès élégantes, des sanitaires PMR modernes et des espaces intégrés esthétiquement qui ne stigmatisent pas les patients à mobilité réduite mais améliorent le confort de tous.</p>""",
        "content_fr": """<h2>L'accessibilité, un pilier de l'aménagement des espaces médicaux</h2>
<p>L'<strong>aménagement d'espaces médicaux</strong> modernes doit inclure dès sa conception l'accessibilité universelle. Au Maroc, la réglementation impose aux établissements recevant du public (ERP), y compris les cabinets et cliniques, de garantir l'accès sans encombre aux personnes à mobilité réduite (PMR).</p>

<h2>1. Les dimensions clés pour un cabinet médical conforme</h2>
<p>Pour obtenir l'autorisation d'ouverture et garantir le confort de tous, plusieurs règles de base doivent être respectées lors de l'<strong>aménagement clinique à Tanger</strong> :</p>
<ul>
    <li><strong>Les portes :</strong> Une largeur minimale de 90 cm pour permettre le passage aisé des fauteuils roulants.</li>
    <li><strong>Les couloirs :</strong> Un espace de circulation d'au moins 1,20 m à 1,40 m de large.</li>
    <li><strong>Les rampes d'accès :</strong> Une pente douce (inférieure à 5% ou 8% selon la longueur) avec mains courantes adaptées.</li>
</ul>

<h2>2. Sanitaires et mobilier adaptés aux normes PMR au Maroc</h2>
<p>L'<strong>accessibilité de votre cabinet médical</strong> s'étend également aux toilettes et au mobilier d'accueil. Les sanitaires doivent disposer d'un espace de rotation d'au moins 1,50 m de diamètre et de barres d'appui installées de façon sécurisée. Le comptoir d'accueil doit comporter une partie abaissée pour le service des patients en fauteuil roulant.</p>

<h2>3. Allier conformité réglementaire et esthétique</h2>
<p>Le respect de la <strong>réglementation sanitaire au Maroc</strong> n'exclut pas le design. Chez MEDICENTERS PERFORMANCE, nous concevons des rampes d'accès élégantes, des sanitaires PMR modernes et des espaces intégrés esthétiquement qui ne stigmatisent pas les patients à mobilité réduite mais améliorent le confort de tous.</p>""",
        "content_en": """<h2>Accessibility: A Pillar of Medical Space Layout</h2>
<p>The <strong>design of medical spaces</strong> must include universal accessibility from the start. In Morocco, regulations require public facilities (ERP), including medical offices and clinics, to guarantee obstacle-free access for persons with reduced mobility (PMR).</p>

<h2>1. Key Dimensions for a Compliant Medical Office</h2>
<p>To obtain operational approval and ensure everyone's comfort, several basic rules must be respected during a <strong>clinic layout in Tangier</strong>:</p>
<ul>
    <li><strong>Doors:</strong> A minimum width of 90 cm to allow easy passage for wheelchairs.</li>
    <li><strong>Corridors:</strong> A circulation space of at least 1.20 m to 1.40 m wide.</li>
    <li><strong>Access Ramps:</strong> A gentle slope (less than 5% or 8% depending on length) with appropriate handrails.</li>
</ul>

<h2>2. Compliant Bathrooms and Furniture under PMR Standards in Morocco</h2>
<p>The <strong>accessibility of your medical office</strong> also extends to toilets and reception furniture. Bathrooms must have a turning circle of at least 1.50 m in diameter and securely installed grab bars. The reception counter must include a lowered section to serve patients in wheelchairs.</p>

<h2>3. Combining Regulatory Compliance with Aesthetics</h2>
<p>Compliance with <strong>health regulations in Morocco</strong> does not exclude design. At MEDICENTERS PERFORMANCE, we design elegant access ramps, modern PMR bathrooms, and aesthetically integrated spaces that improve comfort for everyone without stigmatizing patients with reduced mobility.</p>""",
        "content_ar": """<h2>الولوجيات: ركيزة أساسية لتجهيز المساحات الطبية</h2>
<p>يجب أن يشمل <strong>تجهيز المساحات الطبية</strong> الحديثة منذ البداية معايير الولوجيات الشاملة. في المغرب، يفرض القانون على المؤسسات المستقبلة للعموم (ERP)، بما في ذلك العيادات والمصحات، ضمان وصول الأشخاص ذوي الاحتياجات الخاصة (PMR) دون عوائق.</p>

<h2>1. الأبعاد الأساسية لعيادة طبية مطابقة للمعايير</h2>
<p>للحصول على ترخيص الفتح وضمان راحة الجميع، يجب احترام عدة قواعد أساسية عند <strong>تجهيز عيادة أو مصحة في طنجة</strong>:</p>
<ul>
    <li><strong>الأبواب:</strong> عرض لا يقل عن 90 سم للسماح بمرور الكراسي المتحركة بسهولة.</li>
    <li><strong>الممرات:</strong> مساحة مرور لا تقل عن 1.20 متر إلى 1.40 متر عرضًا.</li>
    <li><strong>ممرات الولوج المائلة:</strong> منحدر خفيف (أقل من 5% أو 8% حسب الطول) مع مقابض يد مناسبة.</li>
</ul>

<h2>2. مرافق صحية وأثاث متوافق مع معايير ذوي الاحتياجات الخاصة في المغرب</h2>
<p>تمتد <strong>ولوجيات العيادة الطبية</strong> أيضًا إلى المراحيض وأثاث الاستقبال. يجب أن تحتوي المرافق الصحية على مساحة دوران لا يقل قطرها عن 1.50 متر وقضبان دعم مثبتة بأمان. كما يجب أن يشتمل مكتب الاستقبال على جزء منخفض لخدمة المرضى على الكراسي المتحركة.</p>

<h2>3. الجمع بين المطابقة القانونية والجمالية</h2>
<p>إن احترام <strong>القوانين الصحية في المغرب</strong> لا يمنع اللمسة الجمالية. في MEDICENTERS PERFORMANCE، نصمم ممرات ولوج أنيقة، ومرافق صحية حديثة متوافقة مع معايير PMR، ومساحات مدمجة بشكل جمالي يحسن راحة الجميع.</p>""",
        "meta_description": "Normes PMR et accessibilité dans l'aménagement d'espaces médicaux au Maroc. Dimensions de portes, couloirs et toilettes conformes à la réglementation.",
        "meta_description_fr": "Normes PMR et accessibilité dans l'aménagement d'espaces médicaux au Maroc. Dimensions de portes, couloirs et toilettes conformes à la réglementation.",
        "meta_description_en": "PMR standards and accessibility in medical space layouts in Morocco. Doors, corridors, and toilet dimensions compliant with health regulations.",
        "meta_description_ar": "معايير الولوجيات وتجهيز المساحات الطبية في المغرب. أبعاد الأبواب والممرات والمراحيض المطابقة للقوانين الصحية المعمول بها.",
        "featured_image_alt": "Rampe d'accès PMR et aménagement clinique au Maroc",
        "featured_image_alt_fr": "Rampe d'accès PMR et aménagement clinique au Maroc",
        "featured_image_alt_en": "PMR access ramp and clinic design in Morocco",
        "featured_image_alt_ar": "ممر ولوج ذوي الاحتياجات الخاصة وتجهيز المصحات في المغرب",
        "author": "MEDICENTERS PERFORMANCE",
        "category_id": 1,
        "is_published": True,
        "published_date": datetime.datetime(2026, 6, 10, 9, 0, tzinfo=datetime.timezone.utc),
        "created_at": datetime.datetime(2026, 6, 10, 9, 0, tzinfo=datetime.timezone.utc),
        "updated_at": datetime.datetime(2026, 6, 10, 9, 0, tzinfo=datetime.timezone.utc),
    },
    {
        "id": 3,
        "title": "Mobilier Médical Sur Mesure : Allier Hygiène et Ergonomie",
        "title_fr": "Mobilier Médical Sur Mesure : Allier Hygiène et Ergonomie",
        "title_en": "Custom Medical Furniture: Combining Hygiene and Ergonomics",
        "title_ar": "الأثاث الطبي المصمم خصيصًا: الجمع بين النظافة وبيئة العمل",
        "slug": "mobilier-medical-sur-mesure-ergonomie",
        "excerpt": "Le choix du mobilier influence directement la confiance des patients et le confort de travail. Découvrez les avantages du mobilier médical sur mesure au Maroc.",
        "excerpt_fr": "Le choix du mobilier influence directement la confiance des patients et le confort de travail. Découvrez les avantages du mobilier médical sur mesure au Maroc.",
        "excerpt_en": "The choice of furniture directly influences patient trust and working comfort. Discover the benefits of custom medical furniture in Morocco.",
        "excerpt_ar": "يؤثر اختيار الأثاث بشكل مباشر على ثقة المرضى وراحة العمل. اكتشف مزايا الأثاث الطبي المصنوع حسب الطلب في المغرب.",
        "content": """<h2>Le mobilier médical, premier vecteur de l'image de votre cabinet</h2>
<p>L'<strong>agencement du mobilier médical</strong> joue un rôle déterminant dans la perception qu'ont les patients de la qualité de vos soins. Que ce soit pour un cabinet de pédiatrie, de gynécologie ou un grand centre de radiologie à Tanger, le choix de meubles adaptés alliant ergonomie et esthétique est crucial.</p>

<h2>1. Le comptoir d'accueil de la clinique : une première impression décisive</h2>
<p>Le <strong>comptoir d'accueil de la clinique</strong> ou du cabinet est le premier point de contact physique avec le patient. Un meuble d'accueil conçu sur mesure doit cacher les écrans et dossiers administratifs pour un aspect propre, tout en restant ouvert et rassurant pour faciliter l'interaction.</p>

<h2>2. Le bureau de consultation du médecin : le confort et l'intimité</h2>
<p>Le <strong>bureau de consultation du médecin</strong> est l'espace où s'établit la relation de confiance. Il doit offrir assez d'espace pour le médecin et le patient, tout en intégrant des espaces de rangement intelligents pour les dossiers et instruments de diagnostic, évitant ainsi le désordre visuel.</p>

<h2>3. L'ergonomie médicale au Maroc et les normes d'hygiène</h2>
<p>Le <strong>mobilier médical sur mesure</strong> doit être fabriqué avec des matériaux spécifiques (panneaux antibactériens, résine acrylique type Corian, absence de joints poreux) pour résister aux agents de désinfection hospitaliers et respecter la réglementation. L'<strong>ergonomie médicale au Maroc</strong> intègre également la posture du praticien pour prévenir les troubles musculosquelettiques (TMS) liés aux longues heures de consultation.</p>""",
        "content_fr": """<h2>Le mobilier médical, premier vecteur de l'image de votre cabinet</h2>
<p>L'<strong>agencement du mobilier médical</strong> joue un rôle déterminant dans la perception qu'ont les patients de la qualité de vos soins. Que ce soit pour un cabinet de pédiatrie, de gynécologie ou un grand centre de radiologie à Tanger, le choix de meubles adaptés alliant ergonomie et esthétique est crucial.</p>

<h2>1. Le comptoir d'accueil de la clinique : une première impression décisive</h2>
<p>Le <strong>comptoir d'accueil de la clinique</strong> ou du cabinet est le premier point de contact physique avec le patient. Un meuble d'accueil conçu sur mesure doit cacher les écrans et dossiers administratifs pour un aspect propre, tout en restant ouvert et rassurant pour faciliter l'interaction.</p>

<h2>2. Le bureau de consultation du médecin : le confort et l'intimité</h2>
<p>Le <strong>bureau de consultation du médecin</strong> est l'espace où s'établit la relation de confiance. Il doit offrir assez d'espace pour le médecin et le patient, tout en intégrant des espaces de rangement intelligents pour les dossiers et instruments de diagnostic, évitant ainsi le désordre visuel.</p>

<h2>3. L'ergonomie médicale au Maroc et les normes d'hygiène</h2>
<p>Le <strong>mobilier médical sur mesure</strong> doit être fabriqué avec des matériaux spécifiques (panneaux antibactériens, résine acrylique type Corian, absence de joints poreux) pour résister aux agents de désinfection hospitaliers et respecter la réglementation. L'<strong>ergonomie médicale au Maroc</strong> intègre également la posture du praticien pour prévenir les troubles musculosquelettiques (TMS) liés aux longues heures de consultation.</p>""",
        "content_en": """<h2>Medical Furniture: The First Impression of Your Practice</h2>
<p>The <strong>arrangement of medical furniture</strong> plays a decisive role in how patients perceive the quality of your care. Whether for a pediatric or gynecological office, or a large radiology center in Tangier, choosing appropriate furniture combining ergonomics and aesthetics is crucial.</p>

<h2>1. The Clinic's Reception Counter: A Decisive First Impression</h2>
<p>The <strong>clinic's reception counter</strong> is the first physical point of contact with the patient. A custom-designed reception desk should conceal screens and administrative files for a clean appearance, while remaining open and welcoming to facilitate interaction.</p>

<h2>2. The Doctor's Consultation Desk: Comfort and Privacy</h2>
<p>The <strong>doctor's consultation desk</strong> is the space where the trust relationship is established. It must offer enough space for both doctor and patient, while integrating smart storage solutions for files and diagnostic instruments to avoid visual clutter.</p>

<h2>3. Medical Ergonomics and Hygiene Standards in Morocco</h2>
<p>Our <strong>custom medical furniture</strong> is manufactured using specific materials (antibacterial panels, acrylic resin like Corian, seamless joints) to withstand hospital-grade disinfectants. <strong>Medical ergonomics in Morocco</strong> also addresses the practitioner's posture to prevent musculoskeletal disorders (MSDs) caused by long consulting hours.</p>""",
        "content_ar": """<h2>الأثاث الطبي: الناقل الأول لصورة عيادتك</h2>
<p>يلعب <strong>تجهيز الأثاث الطبي</strong> دورًا حاسمًا في كيفية إدراك المرضى لجودة رعايتك الصحية. وسواء كان ذلك لعيادة طب الأطفال، طب النساء، أو مركز تصوير إشعاعي كبير في طنجة، فإن اختيار أثاث مناسب يجمع بين الملاءمة والجمال هو أمر بالغ الأهمية.</p>

<h2>1. مكتب استقبال المصحة: انطباع أول حاسم</h2>
<p>يعد <strong>مكتب استقبال المصحة</strong> أو العيادة أول نقطة اتصال مادي مع المريض. يجب أن يخفي مكتب الاستقبال المصمم خصيصًا الشاشات والملفات الإدارية للحصول على مظهر نظيف ومنظم، بينما يظل مفتوحًا ومرحبًا لتسهيل التفاعل.</p>

<h2>2. مكتب استشارة الطبيب: الراحة والخصوصية</h2>
<p>مكتب استشارة الطبيب هو المساحة التي تُبنى فيها علاقة الثقة. يجب أن يوفر مساحة كافية للطبيب والمريض على حد سواء، مع دمج حلول تخزين ذكية للملفات وأدوات التشخيص لتجنب الفوضى البصرية.</p>

<h2>3. بيئة العمل الطبية في المغرب ومعايير النظافة</h2>
<p>يجب تصنيع <strong>الأثاث الطبي المصمم خصيصًا</strong> من مواد خاصة (ألواح مضادة للبكتيريا، راتنج الأكريليك مثل الكوريان، انعدام الفواصل المسامية) لمقاومة معقمات المستشفيات والالتزام باللوائح. وتأخذ <strong>بيئة العمل الطبية في المغرب</strong> بعين الاعتبار وضعية الطبيب لتجنب الاضطرابات العضلية الهيكلية (TMS) الناتجة عن ساعات العمل الطويلة.</p>""",
        "meta_description": "Choisir le mobilier médical sur mesure idéal pour votre clinique au Maroc. Conception de comptoir d'accueil, bureau de médecin et hygiène certifiée.",
        "meta_description_fr": "Choisir le mobilier médical sur mesure idéal pour votre clinique au Maroc. Conception de comptoir d'accueil, bureau de médecin et hygiène certifiée.",
        "meta_description_en": "Choose the perfect custom medical furniture for your clinic in Morocco. Reception counter design, medical desk layout, and certified hygiene.",
        "meta_description_ar": "اختر الأثاث الطبي المصنوع حسب الطلب والمثالي لمصحتك في المغرب. تصميم مكتب الاستقبال ومكاتب الأطباء بنظافة معتمدة.",
        "featured_image_alt": "Bureau de consultation de médecin et comptoir d'accueil sur mesure",
        "featured_image_alt_fr": "Bureau de consultation de médecin et comptoir d'accueil sur mesure",
        "featured_image_alt_en": "Doctor's consultation desk and custom reception counter",
        "featured_image_alt_ar": "مكتب استشارة الطبيب ومكتب استقبال مصنوع حسب الطلب",
        "author": "MEDICENTERS PERFORMANCE",
        "category_id": 1,
        "is_published": True,
        "published_date": datetime.datetime(2026, 6, 20, 9, 0, tzinfo=datetime.timezone.utc),
        "created_at": datetime.datetime(2026, 6, 20, 9, 0, tzinfo=datetime.timezone.utc),
        "updated_at": datetime.datetime(2026, 6, 20, 9, 0, tzinfo=datetime.timezone.utc),
    }
]

# Update local active database
print("Updating database...")
BlogPost.objects.all().delete()
for post_data in new_posts:
    p = BlogPost(**post_data)
    p.save()
    print(f"Created/updated BlogPost in database: {p.title_fr}")

# Update the fixture file (fixtures/initial_data.json)
fixture_path = 'fixtures/initial_data.json'
print(f"Updating fixture {fixture_path}...")
with open(fixture_path, 'r', encoding='utf-8') as f:
    fixture_data = json.load(f)

# Filter out old blogposts and category (if any)
filtered_data = [x for x in fixture_data if x['model'] not in ['blog.blogpost']]

# Re-add category 1 just to be safe
category_fixture = [x for x in fixture_data if x['model'] == 'blog.category' and x['pk'] == 1]
if not category_fixture:
    filtered_data.append({
        "model": "blog.category",
        "pk": 1,
        "fields": {
            "name": "Aménagement Médical",
            "name_fr": "Aménagement Médical",
            "name_en": "Medical Layout",
            "name_ar": "التجهيز الطبي",
            "slug": "amenagement-medical"
        }
    })

# Add the new posts to the fixture data
for p in new_posts:
    fields = p.copy()
    pk = fields.pop('id')
    # convert datetime objects to ISO strings
    for k, v in fields.items():
        if isinstance(v, timezone.datetime):
            fields[k] = v.isoformat().replace("+00:00", "Z")
    
    filtered_data.append({
        "model": "blog.blogpost",
        "pk": pk,
        "fields": fields
    })

# Save updated fixture
with open(fixture_path, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

print("Fixture updated successfully!")
