#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import route
from db import dao 

@route('/stocks/<string:sortField>', methods=['GET'])
def stocks(sortField):
    detail = dao.stocks(sortField)
    
    return detail
        
