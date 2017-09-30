#coding=utf-8

import requests
from time import ctime
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import datetime

#XAG
FUTURE_URL = 'http://www.fx678.com/'

# 获取当前时间
d1 = datetime.datetime.now()
print d1
# 格式化字符串输出
d1str = d1.strftime('%y-%m-%d-%H-%M-%S')
print d1str
# 当前时间加上半小时
#d2 = d1 + datetime.timedelta(hours=0.5)
#print d2
# 格式化字符串输出
#d3 = d2.strftime('%Y-%m-%d %H:%M:%S')
#print d3
# 将字符串转化为时间类型
d4 = datetime.datetime.strptime('2017-09-30 17:44:53.943000','%Y-%m-%d %H:%M:%S.%f')
print d4
