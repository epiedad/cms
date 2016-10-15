from .base import *


DEBUG = False

ADMINS = (
    ('Elianti', 'jelianchaszer@gmail.com'),
)

ALLOWED_HOSTS = ['educa.com', 'www.educa.com','127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '1234'
    }
}
