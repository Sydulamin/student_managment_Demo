"""
Django settings for studen_Managment_system project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p*szl4m-@nt^(_y)9!df(s@14cng21ub%#8ikt_6@r^x^#b=l1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'studen_Managment_system.urls'

AUTH_USER_MODEL = 'Account.CustomUser'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'studen_Managment_system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'new_test',
#         'USER': 'postgres',
#         'PASSWORD': 'root',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [BASE_DIR / 'static', ]
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "My Deshboard",  # Title of the site in the browser tab
    "site_header": "My Dashboard",  # Header displayed at the top
    "site_brand": "My Brand",  # Branding text/logo in the navbar
    "site_logo": "logo.png",  # Path to your logo (from `static` folder)
    "login_logo": "logo.png",  # Logo for the login page
    "login_logo_dark": None,  # Optional dark mode logo for login page
    "site_logo_classes": "img-circle",  # CSS classes for the logo
    "welcome_sign": "Welcome to My Site!",  # Welcome message on login
    "copyright": "My Company © 2024",  # Footer copyright
    "search_model": "auth.User",  # Model to use in the search bar
    "user_avatar": None,  # Avatar field for users
    "topmenu_links": [  # Links in the top navigation bar
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Docs", "url": "https://docs.djangoproject.com/", "new_window": True},
    ],
    "usermenu_links": [  # Links in the user dropdown menu
        {"name": "Support", "url": "https://support.example.com", "new_window": True},
    ],
    "show_sidebar": True,  # Whether to show the sidebar
    "navigation_expanded": True,  # Expand the sidebar menu by default
    "icons": {  # Icons for models in the admin
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "custom_css": None,  # Path to custom CSS file (optional)
    "custom_js": None,  # Path to custom JS file (optional)
    "order_with_respect_to": ["auth", "myapp"],  # Order of apps in the sidebar
}

JAZZMIN_UI_TWEAKS = {
    "navbar": "navbar-dark navbar-primary",  # Navbar styling
    "sidebar": "sidebar-dark-primary",  # Sidebar styling
    "theme": "darkly",  # Optional Bootstrap theme (e.g., 'darkly', 'flatly')
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
    },
    "actions_sticky_top": True,  # Fix action buttons to the top
}
