#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import app
import views

app.debug = True

if __name__ == '__main__':
    app.run()