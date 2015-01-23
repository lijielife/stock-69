#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import route
from db import dao 

@route('/industrys/<int:page>', methods=['GET'])
def industrys(page=0):
    return dao.industrys()


@route('/industry/<string:icode>/<string:sortField>', methods=['GET'])
def industry(icode, sortField):
    detail = dao.industry(icode, sortField)
    
    return {'name':detail[0]['iname'],
            'stocks':detail
            }
        
