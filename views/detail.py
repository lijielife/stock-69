#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import route

@route('/detail')
def detail():
    return 'detail'
        
