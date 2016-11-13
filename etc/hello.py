pythonpath = 'home/box/web'

bind = '0.0.0.0:8080'
backlog = 2048

workers = 1
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 5

errorlog = '/home/box/web/gunicorn.error_log'
loglevel = 'info'
accesslog = '/home/box/web/gunicorn.access_log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'