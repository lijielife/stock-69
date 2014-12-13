#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Numeric
from db import Base, db_session

class Stock(Base):
    __tablename__ = 'stocks'
    sid = Column(String, primary_key=True)
    name = Column(String(32))
    price = Column(Numeric(scale=3))
    industry = Column(String(32))

    def __init__(self, sid=None, name=None, price=None, industry=None):
        self.sid = sid
        self.name = name
        self.price = price
        self.industry = industry

    def __repr__(self):
        return '<Stock sid=%s, name=%s>' % (self.sid, self.name)

s = Stock(sid='123', name='abc', price='15.01', industry='bb')
print Stock.query.all()
