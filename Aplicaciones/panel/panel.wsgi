import sys
import os
import bottle
import beaker.middleware

import panel

sys.path = ['/var/www/html/panel/'] + sys.path
os.chdir(os.path.dirname(__file__))

# Inicialice app with SessionMiddleware environ
application = beaker.middleware.SessionMiddleware(bottle.default_app(), panel.session_opts)
