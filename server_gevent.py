#!/usr/bin/env python
# -*- coding: utf-8 -*-
import views
from application import app
from gevent.wsgi import WSGIServer
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()