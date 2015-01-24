#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.sql import text
from sqlalchemy import create_engine

engine = create_engine('mysql://stock:zaq12wsx@localhost/stock?charset=utf8', convert_unicode=True)



def industrys():
    with engine.connect() as conn:
        cmd = 'select * from industry'
        result = conn.execute(text(cmd))
        
        rows = []
        for row in result:
            ids = dict()
            
            if row['code'] != "" and row['name'] != "":
                ids['code'] = row['code']
                ids['name'] = row['name']                
                rows.append(ids)
        
        return rows

def industry(icode, sortField):
    with engine.connect() as conn:
        sf = sortField
        if sortField != 'pe_lyr' and sortField != 'pe_ttm' and sortField != 'pb' and sortField != 'psr':
            sf = 'pe_lyr'
              
        cmd = 'select s.*,i.name as iname from stock s, industry i where s.icode = i.code and s.icode = :code and ' + sf + ' is not null order by ' + sf
        result = conn.execute(text(cmd),
                              code=icode)
        
        rows = []
        for row in result:
            ids = dict()
            
            if row['code'] != "" and row['name'] != "":
                ids['code'] = row['code']
                ids['name'] = row['name']
                ids['iname'] = row['iname']
                ids['price'] = row['price'].to_eng_string()
                ids['sf'] = '--' if not row[sf] else row[sf].to_eng_string()
              
                rows.append(ids)

        return rows
    
    
def stock(code):
    with engine.connect() as conn:
        cmd = 'select s.*,i.name as iname from stock s, industry i where s.icode = i.code and s.code = :cd'
        result = conn.execute(text(cmd),
                              cd=code)
        
        for row in result:
            ids = dict()
            
            if row['code'] != "" and row['name'] != "":
                ids['code'] = row['code']
                ids['name'] = row['name']
                ids['iname'] = row['iname'] if len(row['iname']) <= 4 else row['iname'][0:4] + '...'
                ids['price'] = row['price'].to_eng_string()
                ids['total_amount'] = (int(row['totalShares']) * row['price'] / 100000000).to_integral().to_eng_string()
                ids['totalShares'] = row['totalShares']
                ids['float_shares'] = row['float_shares']
                ids['eps'] = row['eps']
                ids['dividend'] = row['dividend']
                ids['net_assets'] = row['net_assets']
                ids['pe_lyr'] = '--' if not row['pe_lyr'] else row['pe_lyr'].to_eng_string()
                ids['pe_ttm'] = '--' if not row['pe_ttm'] else row['pe_ttm'].to_eng_string()
                ids['pb'] = '--' if not row['pb'] else row['pb'].to_eng_string()
                ids['psr'] = '--' if not row['psr'] else row['psr'].to_eng_string()
              
                return ids
