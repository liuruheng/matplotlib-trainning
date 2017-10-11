#coding=utf-8

import requests
import time
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import datetime

#XAG
FUTURE_URL = 'http://www.fx678.com/'
#汇通网报价
FX678_XAG_URL = 'http://api.q.fx678.com/quotes.php?exchName=WGJS&symbol=XAG'
FX678_XAU_URL = 'http://api.q.fx678.com/quotes.php?exchName=WGJS&symbol=XAU'
# 开盘价 --- p
# 最新价 --- b
# 最高价 --- h
# 最低价 --- l
# 时间戳 --- t
# 买入价 --- b
# 卖出价 --- se

#金十报价墙
JIN10_PRICE_WALL = 'https://www.jin10.com/price_wall/index.html'
#安全socket连接中包含报价信息
#https://ssgfcfkdll.jin10.com:9081/socket.io/?EIO=3&transport=polling&t=LxSsrnb&sid=CI8hf7hc-WLfuazjABqN

def getGMTBEIJINGTime():
    '''获取当前时间'''
    d1 = datetime.datetime.now()
    print d1
    # 格式化字符串输出
    d1str = d1.strftime('%y-%m-%d-%H-%M-%S')
    print d1str
    # 当前时间加上半小时
    #d2 = d1 + datetime.timedelta(hours=0.5)
    # 格式化字符串输出
    #d3 = d2.strftime('%Y-%m-%d %H:%M:%S')
    # 将字符串转化为时间类型
    d4 = datetime.datetime.strptime('2017-09-30 17:44:53.943000','%Y-%m-%d %H:%M:%S.%f')

def queryInfo(url):
    '''获取信息'''
    try:
        r = requests.get(url)
        content = r.text.split('{')[1].split('}')[0].split(',')
        print content
        tag = []
        value = []

        for item in content:
            tag.append(item.split(':')[0])
            #以下两种写法效果相同
            value.append(item.split(':')[1].strip('[""]'))
            #value.append(re.sub('\"]', '', re.sub('\["', '', item.split(':')[1])))

        #for i in range(len(content)):
            #print "%s  %s" % (content[i].split(':')[0], content[i].split(':')[1])
            #print re.search('\[', content[i].split(':')[1])
            #print re.sub('\[', '', content[i].split(':')[1])

        infoDict = dict(zip(tag,value))
        print infoDict
        print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(infoDict[u'"t"'])))
    except (Exception),e:
        print "Exception: "+e.message
        return ""

queryInfo(FX678_XAG_URL)