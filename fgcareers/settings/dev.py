from .base import *

DEBUG = True

SECRET_KEY = 'h0n_fv+q46(-)k@q!g78z9(fb9+*d=0aj$klk4mddbv_6ab*l2'

ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass 