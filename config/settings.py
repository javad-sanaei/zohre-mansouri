import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ===== SECURITY =====
# ⚠️ کلید از متغیر محیطی خونده می‌شه. اگه نبود، از کلید پیش‌فرض استفاده می‌کنه (فقط برای لوکال)
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-px$fv308py5zi^^_&0o*un)3=1x0g@t==2_a8@!_)k*d8=7k02'
)

# ⚠️ توی Render مقدار DEBUG=False ست می‌شه
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ⚠️ دامنه‌های مجاز
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
    'zohremansouri.ir',
    'www.zohremansouri.ir',
]

# ===== CSRF TRUSTED ORIGINS (برای فرم‌های POST) =====
CSRF_TRUSTED_ORIGINS = [
    'https://zohremansouri.ir',
    'https://www.zohremansouri.ir',
    'https://*.onrender.com',
]

# ===== INSTALLED APPS =====
INSTALLED_APPS = [
    # Django built-in
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # اپ‌های ما
    'apps.core',
    'apps.blog',
    'apps.contact',
    'apps.testimonials',
    'apps.comments',

    # پکیج‌های جانبی
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ← اضافه شد
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# ===== DATABASE =====
# توی لوکال از SQLite استفاده می‌کنه، توی Render از PostgreSQL
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        ssl_require=not DEBUG,   # توی production SSL لازمه
    )
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# ===== STATIC & MEDIA =====
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise برای فشرده‌سازی و سرو static توی production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===== CKEDITOR =====
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
        'language': 'fa',
    },
}

# ===== SECURITY (فقط توی production) =====
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000  # 1 سال
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')