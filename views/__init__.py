#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.home import home_blueprint
from views.detail import detail_blueprint

views = (
         home_blueprint,
         detail_blueprint,
)