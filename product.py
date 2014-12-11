#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views import views
from flask import Flask


app = Flask(__name__)

for view in views:
    app.register_blueprint(view)

if __name__ == '__main__':
    app.run()
