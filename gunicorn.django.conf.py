command = '/home/box/web/etc/web_venv/bin/gunicorn'
pythonpath = '/home/box/web/ask'
bind = "0.0.0.0:8000"
pidfile = 'gunicorn.django.pid'
workers = 3
