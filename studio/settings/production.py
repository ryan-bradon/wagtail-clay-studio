from .base import *

DEBUG = False
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

try:
    from .local import *
except ImportError:
    pass
