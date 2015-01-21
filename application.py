#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)
route = app.route
