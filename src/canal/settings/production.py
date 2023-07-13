from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['api.canal.ink',
                 'www.canal.ink',
                 'canal.ink',
                 'localhost', '127.0.0.1',
                 'canal-prod-elb-1788944198.ap-northeast-1.elb.amazonaws.com',]

# ADMINS = [
#     ('Hiroto', 'hirotoaoki1349@gmail.com'),
# ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': os.environ["CANAL_DB_HOST"],
#         'PORT': os.environ["CANAL_DB_PORT"],
#         'NAME': 'canal',
#         'USER': os.environ["CANAL_DB_USER"],
#         'PASSWORD': os.environ["CANAL_DB_PASSWORD"],
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#             'use_unicode': True,
#         },
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': "localhost",
        'PORT': "3306",
        'NAME': 'canal',
        'USER': "root",
        'PASSWORD': "family1224",
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'use_unicode': True,
        },
    }
}

INTERNAL_IPS = ["127.0.0.1", ]
