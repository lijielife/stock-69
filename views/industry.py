#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import route

@route('/industrys/<int:page>', methods=['GET'])
def industry_list(page=0):
    return [{
             'icode':'abc',
             'name':u'金融行业'
             },
             {
              'icode':'xyz',
              'name':u'房地产行业'
            }]


@route('/industry/<string:icode>', methods=['GET'])
def industry(icode):
    return {'icode': icode,
            'name':u'金融行业',
            'stocks':[
                      {'code':'000783',
                       'name':u'长江证券',
                       'price': 15.53},
                      {'code':'600030',
                       'name':u'中信证券',
                       'price':19.32}]}
        
