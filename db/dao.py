#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.sql import text
from sqlalchemy import create_engine, Column, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, load_only
from datetime import datetime

engine = create_engine('mysql://stock:zaq12wsx@localhost/stock?charset=utf8', convert_unicode=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

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

def stocks(sortField):
    with engine.connect() as conn:
        sf = sortField
        if sortField != 'pe_lyr' and sortField != 'pe_ttm' and sortField != 'pb' and sortField != 'psr':
            sf = 'pe_lyr'
              
        cmd = 'select * from stock where ' + sf + ' is not null order by ' + sf + ' limit 50'
        result = conn.execute(text(cmd))
        
        rows = []
        for row in result:
            ids = dict()
            
            if row['code'] != "" and row['name'] != "":
                ids['code'] = row['code']
                ids['name'] = row['name']
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

def load_stocks():
    ses = Session()
    return ses.query(Stock).options(load_only(Stock.code)).all()

def save_stock(item):
    stock = Stock(code=item['code'],
                  name=item['name'],
                  price=item['price'],
                  totalShares=item['totalShares'],  # 总股本：122.60亿
                  float_shares=item['float_shares'],  # 流通股本：101.26亿
                  eps=item['eps'],  # 每股收益：0.35
                  dividend=item['dividend'],  # 每股股息：0.20
                  net_assets=item['net_assets'],  # 每股净资产：3.87
                  pe_lyr=None if item['pe_lyr'] == '' else item['pe_lyr'],  # 市盈率LYR：40.88
                  pe_ttm=None if item['pe_ttm'] == '' else item['pe_ttm'],  # 市盈率TTM：30.32
                  pb=None if item['pb'] == '' else item['pb'],  # 市净率TTM：3.64
                  psr=None if item['psr'] == '' else item['psr'],  # 市销率TTM
                  update_time=datetime.now())
    
    ses = Session()
    stock = ses.merge(stock)
    
    if not stock.create_time:
        stock.create_time = datetime.now()
        
    ses.commit()
    
class Stock(Base):
    __tablename__ = 'stock'
    code = Column(String(16), primary_key=True)  # 股票代码
    name = Column(String(16))  # 股票名字
    icode = Column(String(16))  # 行业code
    price = Column(Numeric(10, 3))  # 价格
    totalShares = Column(String(16))  # 总股本：122.60亿
    float_shares = Column(String(16))  # 流通股本：101.26亿
    eps = Column(String(16))  # 每股收益：0.35
    dividend = Column(String(16))  # 每股股息：0.20
    net_assets = Column(String(16))  # 每股净资产：3.87
    pe_lyr = Column(Numeric(12, 4))  # 市盈率LYR：40.88
    pe_ttm = Column(Numeric(12, 4))  # 市盈率TTM：30.32
    pb = Column(Numeric(12, 4))  # 市净率TTM：3.64
    psr = Column(Numeric(12, 4))  # 市销率TTM：1.62
    create_time = Column(DateTime)  # 创建时间
    update_time = Column(DateTime)  # 更新时间

    def __repr__(self):
        return '<Stock %s:%s>' % (self.code, self.name)
    