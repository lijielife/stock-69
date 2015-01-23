#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import route
from db import dao

@route('/stock/<string:code>', methods=['GET'])
def stock(code):
    return dao.stock(code)
