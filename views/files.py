#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, send_from_directory
from application import route, app

@route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])