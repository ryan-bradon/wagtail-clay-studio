from .base import *
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z_dvidaz2f%j0puq*$3l33b+94ca*02sxg5g1wq!3+xxux_j48"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["king-prawn-app-n4d8w.ondigitalocean.app", "art.fosho.org",
                 "127.0.0.1", "localhost", ]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if not DEBUG:
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_REFERRER_POLICY = 'same-origin'
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
