import os
import sys
import django

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
django.setup()

from apps.recruitment.models import JobPosting

# 1. We keep the existing telephone secretary stage if it exists, or create/recreate it
sec_job = JobPosting.objects.filter(slug="offre-stage-secretaire-commercial-telephonique").first()
if not sec_job:
    sec_job = JobPosting.objects.create(
        title="Offre de Stage – Secrétaire & Commercial(e) Téléphonique",
        slug="offre-stage-secretaire-commercial-telephonique",
        department="Administration & Relation Client",
        location="Tanger, Maroc",
        contract_type="Stage",
        description="Rejoignez notre équipe de communication pour un stage enrichissant au sein de notre entreprise. Vous participerez aux missions de secrétariat et de téléphonie commerciale en assurant l'accueil téléphonique, la gestion des rendez-vous, le suivi administratif des dossiers, la prospection et les relances téléphoniques, ainsi que l'accompagnement de nos clients et prospects. Cette expérience vous permettra de développer vos compétences en communication, en relation client et en gestion administrative dans un environnement professionnel dynamique.",
        requirements="- Étudiante ou lauréate en secrétariat, gestion, commerce ou domaine similaire.\n- Excellente maîtrise du français à l'oral et à l'écrit.\n- Aisance téléphonique et sens du relationnel.\n- Maîtrise des outils bureautiques (Word, Excel, Outlook).\n- Organisée, rigoureuse, dynamique et motivée.\n- Esprit d'équipe et sens des responsabilités.\n- Stage rémunéré.",
        is_active=True
    )
sec_job.title_fr = "Offre de Stage – Secrétaire & Commercial(e) Téléphonique"
sec_job.title_en = "Internship Opportunity – Secretary & Telephone Sales Representative"
sec_job.title_ar = "فرصة تدريب – سكرتيرة وممثلة مبيعات عبر الهاتف"
sec_job.department_fr = "Administration & Relation Client"
sec_job.department_en = "Administration & Client Relations"
sec_job.department_ar = "الإدارة وعلاقات العملاء"
sec_job.save()
print("Saved/retained Job 1 (Secrétaire & Commerciale).")

# 2. Restore Job 2: Interior Architect
arch_job = JobPosting.objects.filter(slug="architecte-interieur-medical").first()
if not arch_job:
    arch_job = JobPosting.objects.create(
        title="Architecte d'intérieur – Spécialisation médicale",
        slug="architecte-interieur-medical",
        department="Design & Architecture",
        location="Tanger, Maroc",
        contract_type="CDI",
        description="Nous recherchons un(e) architecte d'intérieur passionné(e) par le secteur médical pour rejoindre notre équipe de conception. Vous serez responsable de la création de plans d'aménagement pour des cliniques, cabinets médicaux et laboratoires, en intégrant les normes sanitaires et les besoins fonctionnels spécifiques au secteur de la santé.",
        requirements="- Diplôme en architecture d'intérieur ou design d'espace\n- Minimum 3 ans d'expérience en aménagement d'espaces professionnels\n- Maîtrise d'AutoCAD, SketchUp et des logiciels de rendu 3D\n- Connaissance des normes d'accessibilité et de sécurité\n- Sens de l'esthétique et attention aux détails\n- Français courant, arabe apprécié",
        is_active=True
    )
arch_job.title_fr = "Architecte d'intérieur – Spécialisation médicale"
arch_job.title_en = "Interior Architect – Medical Specialization"
arch_job.title_ar = "مهندس معماري داخلي - تخصص طبي"
arch_job.department_fr = "Design & Architecture"
arch_job.department_en = "Design & Architecture"
arch_job.department_ar = "التصميم والهندسة المعمارية"
arch_job.description_fr = "Nous recherchons un(e) architecte d'intérieur passionné(e) par le secteur médical pour rejoindre notre équipe de conception. Vous serez responsable de la création de plans d'aménagement pour des cliniques, cabinets médicaux et laboratoires, en intégrant les normes sanitaires et les besoins fonctionnels spécifiques au secteur de la santé."
arch_job.description_en = "We are looking for an interior architect passionate about the medical sector to join our design team. You will be responsible for creating design plans for clinics, medical offices, and laboratories, integrating health standards and functional needs specific to the healthcare sector."
arch_job.description_ar = "نحن نبحث عن مهندس معماري داخلي شغوف بالقطاع الطبي للانضمام إلى فريق التصميم لدينا. ستكون مسؤولاً عن إنشاء مخططات تجهيز وتصميم للعيادات والمكاتب الطبية والمختبرات، مع دمج المعايير الصحية والاحتياجات الوظيفية الخاصة بقطاع الرعاية الصحية."
arch_job.requirements_fr = "- Diplôme en architecture d'intérieur ou design d'espace\n- Minimum 3 ans d'expérience en aménagement d'espaces professionnels\n- Maîtrise d'AutoCAD, SketchUp et des logiciels de rendu 3D\n- Connaissance des normes d'accessibilité et de sécurité\n- Sens de l'esthétique et attention aux détails\n- Français courant, arabe apprécié"
arch_job.requirements_en = "- Degree in interior architecture or space design\n- Minimum 3 years of experience in professional space planning\n- Proficiency in AutoCAD, SketchUp, and 3D rendering software\n- Knowledge of accessibility and safety standards\n- Aesthetic sense and attention to detail\n- Fluent French, Arabic appreciated"
arch_job.requirements_ar = "- شهادة في الهندسة المعمارية الداخلية أو تصميم الفضاءات\n- خبرة لا تقل عن 3 سنوات في تجهيز وتخطيط المساحات المهنية\n- إتقان برامج AutoCAD و SketchUp وبرامج الرسوم ثلاثية الأبعاد 3D\n- معرفة بمعايير السلامة والولوجيات لذوي الاحتياجات الخاصة\n- حس جمالي واهتمام بالتفاصيل\n- إتقان اللغة الفرنسية، ومعرفة باللغة العربية ميزة إضافية"
arch_job.save()
print("Saved/restored Job 2 (Architecte d'intérieur).")

# 3. Restore Job 3: B2B Sales Representative
sales_job = JobPosting.objects.filter(slug="commercial-b2b-medical").first()
if not sales_job:
    sales_job = JobPosting.objects.create(
        title="Commercial B2B – Secteur médical",
        slug="commercial-b2b-medical",
        department="Commercial & Ventes",
        location="Tanger, Maroc",
        contract_type="CDI",
        description="MEDICENTERS PERFORMANCE recherche un(e) commercial(e) B2B dynamique pour développer notre portefeuille de clients dans le secteur de la santé au Maroc. Vous prospecterez des cliniques, cabinets médicaux, pharmacies et laboratoires pour leur proposer nos solutions d'aménagement et de consulting.",
        requirements="- Formation commerciale (Bac+3 minimum)\n- Expérience de 2 ans en vente B2B, idéalement dans le secteur médical ou de l'aménagement\n- Excellentes compétences en négociation et en relation client\n- Autonomie et capacité à gérer un territoire commercial\n- Permis de conduire et véhicule\n- Français et arabe courants",
        is_active=True
    )
sales_job.title_fr = "Commercial B2B – Secteur médical"
sales_job.title_en = "B2B Sales Representative – Medical Sector"
sales_job.title_ar = "مندوب مبيعات B2B - القطاع الطبي"
sales_job.department_fr = "Commercial & Ventes"
sales_job.department_en = "Sales & Business Development"
sales_job.department_ar = "المبيعات وتطوير الأعمال"
sales_job.description_fr = "MEDICENTERS PERFORMANCE recherche un(e) commercial(e) B2B dynamique pour développer notre portefeuille de clients dans le secteur de la santé au Maroc. Vous prospecterez des cliniques, cabinets médicaux, pharmacies et laboratoires pour leur proposer nos solutions d'aménagement et de consulting."
sales_job.description_en = "MEDICENTERS PERFORMANCE is looking for a dynamic B2B sales representative to develop our client portfolio in the healthcare sector in Morocco. You will prospect clinics, medical offices, pharmacies, and laboratories to offer them our design and consulting solutions."
sales_job.description_ar = "تبحث MEDICENTERS PERFORMANCE عن مندوب مبيعات B2B ديناميكي لتطوير محفظة عملائنا في قطاع الرعاية الصحية في المغرب. ستقوم بالتنقيب والبحث عن العيادات والمكاتب الطبية والصيدليات والمختبرات لتقديم حلول التجهيز والاستشارات الخاصة بنا."
sales_job.requirements_fr = "- Formation commerciale (Bac+3 minimum)\n- Expérience de 2 ans en vente B2B, idéalement dans le secteur médical ou de l'aménagement\n- Excellentes compétences en négociation et en relation client\n- Autonomie et capacité à gérer un territoire commercial\n- Permis de conduire et véhicule\n- Français et arabe courants"
sales_job.requirements_en = "- Business degree (Bachelor's degree minimum)\n- 2 years of experience in B2B sales, ideally in the medical or interior fitting sector\n- Excellent negotiation and customer relation skills\n- Autonomy and ability to manage a commercial territory\n- Driving license and vehicle\n- Fluent French and Arabic"
sales_job.requirements_ar = "- تكوين في مجال التجارة والمبيعات (بكالوريوس على الأقل)\n- خبرة سنتين في المبيعات بين الشركات (B2B)، ويفضل أن تكون في القطاع الطبي أو التجهيز\n- مهارات ممتازة في التفاوض وبناء العلاقات مع العملاء\n- الاستقلالية والقدرة على إدارة منطقة تجارية\n- رخصة قيادة وسيارة\n- إتقان اللغتين الفرنسية والعربية"
sales_job.save()
print("Saved/restored Job 3 (Commercial B2B).")

print("All 3 jobs successfully set up in the database.")
