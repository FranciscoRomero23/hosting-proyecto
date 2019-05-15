import sys
import os
import bottle
import beaker.middleware

import hosting

sys.path = ['/var/www/html/hosting/'] + sys.path
os.chdir(os.path.dirname(__file__))

# Inicialice app with SessionMiddleware environ
application = beaker.middleware.SessionMiddleware(bottle.default_app(), hosting.session_opts)
