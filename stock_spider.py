# -*- coding: utf-8 -*-
import json, time, urllib2
from urllib2 import URLError
from db import dao
from db.dao import save_stock

def scan():
    stocks = dao.load_stocks()
    
    url_stock = 'https://xueqiu.com/stock/quote.json?code=%s&_=%s'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'    
    headers = {'User-Agent' : user_agent,
               'Cookie':'87123wuwnl; xq_a_token=b8d18e01dc28a758fd4659f5c100f1eafaddde13; xq_r_token=6d8d9fc5cfd2c5537575644172bbf81be2c86321'
    }
    
    for st in stocks:
        time.sleep(3)
        
        try:
            url = url_stock % (st.code.upper(), int(time.time() * 1000))
            req = urllib2.Request(url, None, headers)    
            response = urllib2.urlopen(req)  
            body = response.read()
            if response.getcode() == 200:
                data = json.loads(body)
                quotes = data.get('quotes')
                if quotes :
                    if len(quotes) > 0:
                        stock = quotes[0]
                        item = {}
                        item['code'] = stock['symbol'].lower()               
                        item['name'] = stock['name']
                        item['price'] = stock['current']
                        item['totalShares'] = stock['totalShares']  # 总股本：122.60亿
                        item['float_shares'] = stock['float_shares']  # 流通股本：101.26亿
                        item['eps'] = stock['eps']  # 每股收益：0.35
                        item['dividend'] = stock['dividend']  # 每股股息：0.20
                        item['net_assets'] = stock['net_assets']  # 每股净资产：3.87
                        item['pe_lyr'] = stock['pe_lyr']  # 市盈率LYR：40.88
                        item['pe_ttm'] = stock['pe_ttm']  # 市盈率TTM：30.32
                        item['pb'] = stock['pb']  # 市净率TTM：3.64
                        item['psr'] = stock['psr']  # 市销率TTM：1.62
                        
                        save_stock(item)
        except URLError, e:
            print e.reason
                    
scan()
