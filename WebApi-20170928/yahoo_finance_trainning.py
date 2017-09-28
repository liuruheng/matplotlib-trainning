#coding=utf-8
import requests
from time import ctime
from urllib2 import urlopen

def silver_futures():
    silver_url = "https://finance.yahoo.com/quote/SI=F?p=SI=F"
    print("Silver Status code:", requests.get(silver_url).status_code)

TICKs = ('yhoo', 'dell', 'cost', 'adbe')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'
print(URL % ','.join(TICKs))
print '\nPrices quoted as of:%s PDT\n' %ctime()
print 'TICKER', 'PRICE', 'CHANGE', '%AGE'
print '------','------','------','------'

r = requests.get(URL)
print("Status code:", r.status_code)

u = urlopen(URL%','.join(TICKs))

for row in u:
    tick, price, chg, per = row.split(',')
    print tick, price, chg, per

silver_futures()
u.close()

