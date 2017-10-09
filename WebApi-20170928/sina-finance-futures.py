# -*- coding:utf-8 -*-

import requests
from time import ctime
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

#伦敦金
XAU_URL='http://finance.sina.com.cn/futures/quotes/XAU.shtml'
#伦敦银
XAG_URL='http://finance.sina.com.cn/futures/quotes/XAG.shtml'
#新浪报价
# XAU-JS
SINA_XAG_JS_URL = 'http://hq.sinajs.cn/&list=hf_XAU'
#XAG-JS
SINA_XAG_JS_URL = 'http://hq.sinajs.cn/&list=hf_XAG'
#JS_Dict
JS_DICT = ['real-price','wave-rate','buy','sell','max-price','min-price',
           'trade-end-time','yestoday-price','close-price',
           'amount','volume','buy-amount','sell-amount']
#JS_DICT = ['最新价','涨跌率','买价','卖价','最高价','最低价',
#           '收盘时间','昨结算','收盘价','持仓量','成交量','买入量','卖出量']
def getXAGHTMLText(url):
    """获取伦敦银HTML页面"""
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getXAGInfo(url):
    """获取伦敦银的相关信息"""
    html = getXAGHTMLText(url)
    if html == "":
        print('获取HTML页面:' + url + ' 失败')
        return
    print('获取HTML页面:' + url + ' 成功')

    #try:
    infoDict = {}
    soup = BeautifulSoup(html,'html.parser')
    stockInfo = soup.find('div',attrs={'id':'box-futures-hq-wrap'})
    print(stockInfo)
    #找到相关信息项
    keyList = stockInfo.find_all('td')
    valueList = stockInfo.find_all('th')
    #存入字典中
    for i in range(len(keyList)):
        key = keyList[i].text
        val = valueList[i].text
        infoDict[key] = val
    print(infoDict)
    #except:
    #    print('有异常产生')

def getXAGJS():
    '''从JS中获取现货白银报价等相关信息'''
    r = requests.get(XAG_JS_URL)
    print("Status code:", r.status_code)

    u = urlopen(XAG_JS_URL)

    js_content = (u.read().split('='))[1].split(',')
    js_dict = dict(zip(JS_DICT,js_content))

    print js_dict.keys()

    for i in js_dict:
        print js_dict[i]

    print js_dict.items()
    print list(js_dict.iteritems())

def main():
    #getXAGInfo(XAG_URL)
    getXAGJS()

main()