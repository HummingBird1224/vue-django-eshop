import os

if os.environ.get('CANAL_DEBUG', None) == 'True':
    print("__DEBUG MODE__")
    from .dev import *
else:
    from .production import *
