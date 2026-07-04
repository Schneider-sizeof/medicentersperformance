# MEDICENTERS PERFORMANCE — Website

Production-grade Django website for **MEDICENTERS PERFORMANCE**, a B2B interior fit-out, furniture supply, and consulting company for medical professional spaces based in Tangier, Morocco.

## Tech Stack

- **Backend:** Django 5.1, Python 3.12
- **Database:** PostgreSQL (production) / SQLite (development)
- **i18n:** django-modeltranslation (DB content) + Django i18n (template strings) — FR, AR (RTL), EN
- **Frontend:** Bootstrap 5.3 (with RTL support), custom CSS, vanilla JavaScript
- **Rich Text:** django-ckeditor-5
- **Static Files:** WhiteNoise
- **SEO:** django.contrib.sitemaps, Schema.org JSON-LD, hreflang tags

## Quick Start

### 1. Clone & Setup Environment

```bash
# Clone the repository
git clone <repo-url>
cd MedicentersPerformance

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
copy .env.example .env
# Edit .env with your settings (SECRET_KEY, etc.)
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Load Seed Data

```bash
python manage.py loaddata fixtures/initial_data.json
```

### 6. Create Admin User

```bash
python manage.py createsuperuser
```

### 7. Place the Logo

Copy the company logo to:
```
static/images/logo.png
```

### 8. Run Development Server

```bash
python manage.py runserver
```

- **Site:** http://localhost:8000/fr/
- **Admin:** http://localhost:8000/fr/admin/

## Project Structure

```
MedicentersPerformance/
├── manage.py
├── requirements.txt
├── .env.example
├── medicenters_project/          # Django project config
│   ├── settings/
│   │   ├── base.py               # Shared settings
│   │   ├── dev.py                # Development (SQLite)
│   │   └── prod.py               # Production (PostgreSQL)
│   ├── urls.py                   # Root URLs with i18n_patterns
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── core/                     # Home, About, company info, sitemaps
│   ├── services/                 # Service categories
│   ├── blog/                     # Blog posts with CKEditor
│   ├── recruitment/              # Job postings & applications
│   └── contact/                  # Contact form & messages
├── templates/                    # All Django templates
│   ├── base.html                 # Master template (RTL-aware)
│   ├── includes/                 # Navbar, footer, SEO, breadcrumbs, Matterport
│   ├── core/                     # Home, About pages
│   ├── services/                 # Services page
│   ├── blog/                     # Blog list & detail
│   ├── recruitment/              # Careers & application
│   └── contact/                  # Contact form
├── static/
│   ├── css/style.css             # Custom brand stylesheet
│   ├── js/main.js                # Animations, lazy loading, UI
│   └── images/logo.png           # Company logo (place here)
├── fixtures/
│   └── initial_data.json         # Seed data
└── locale/                       # Translation .po/.mo files
```

## Translation Management

### Static Template Strings ({% trans %})

```bash
# Generate message files for Arabic and English
python manage.py makemessages -l ar -l en

# Edit locale/ar/LC_MESSAGES/django.po and locale/en/LC_MESSAGES/django.po

# Compile translations
python manage.py compilemessages
```

### Database Content (django-modeltranslation)

Content is managed in the Django admin. Each model with translatable fields shows tabbed language inputs for FR, AR, and EN.

## Matterport Integration

Virtual 3D tours are managed via the **Showroom** model in the admin:

1. Go to Admin → Core & Pages → Showrooms virtuels
2. Add a new Showroom with the Matterport Showcase URL:
   `https://my.matterport.com/show/?m=YOUR_SPACE_ID`
3. Check "Afficher en page d'accueil" to feature it on the home page
4. The iframe loads lazily and is fully responsive (16:9)

## Production Deployment

1. Set `DJANGO_SETTINGS_MODULE=medicenters_project.settings.prod`
2. Configure PostgreSQL credentials in `.env`
3. Configure SMTP email settings in `.env`
4. Set `SECRET_KEY` to a secure random string
5. Set `ALLOWED_HOSTS` to your domain
6. Run `python manage.py collectstatic`
7. Deploy with Gunicorn + Nginx

## Apps Overview

| App | Purpose |
|-----|---------|
| `core` | Home page, About page, company info singleton, testimonials, Matterport showrooms, sitemaps |
| `services` | 6 service categories with descriptions, managed from admin |
| `blog` | Blog posts with rich text (CKEditor 5), categories, pagination |
| `recruitment` | Job postings + application form with CV upload, honeypot & captcha spam protection |
| `contact` | Contact form with email notification, honeypot & captcha spam protection |
