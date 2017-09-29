#coding=utf-8

import requests
from time import ctime
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

#伦敦金
XAU_URL='http://finance.sina.com.cn/futures/quotes/XAU.shtml'
#伦敦银
XAG_URL='http://finance.sina.com.cn/futures/quotes/XAG.shtml'

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

def main():
    getXAGInfo(XAG_URL)

main()