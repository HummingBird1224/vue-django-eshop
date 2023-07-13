from .base import *

ALLOWED_HOSTS = ['api.canal.ink',
                 'staging.canal.ink',
                 'dev.canal.ink',
                 'internal.canal.ink',
                 'www.canal.ink',
                 'canal.ink',
                 'localhost',
                 '127.0.0.1',]

ROOT_URLCONF = 'canal.urls_dev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ["CANAL_DB_HOST"],
        'PORT': os.environ["CANAL_DB_PORT"],
        'NAME': 'canal',
        'USER': os.environ["CANAL_DB_USER"],
        'PASSWORD': os.environ["CANAL_DB_PASSWORD"],
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'use_unicode': True,
        },
    }
}

INTERNAL_IPS = ["127.0.0.1"]

ALLOWED_HOSTS = ['*']
