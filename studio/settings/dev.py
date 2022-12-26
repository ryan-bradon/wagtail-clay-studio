from .base import *
import dotenv

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z_dvidaz2f%j0puq*$3l33b+94ca*02sxg5g1wq!3+xxux_j48"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["king-prawn-app-n4d8w.ondigitalocean.app", "art.fosho.org",
                 "127.0.0.1", "localhost", ]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except ImportError:
    pass
