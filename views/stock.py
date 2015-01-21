#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import route

@route('/stock/<string:code>', methods=['GET'])
def stock(code):
    if code == '000783':
        return {'code': code,
                'name':u'长江证券',
                'price':15.05}
    else:
        return {'code': code,
                'name':u'中信证券',
                'price':19.23}
