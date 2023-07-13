#!/usr/bin/env bash
cd /suez/src/
python3 manage.py migrate
# gunicorn --workers 4 canal.wsgi --bind=0.0.0.0:8000
python3 manage.py runserver 0.0.0.0:8000

