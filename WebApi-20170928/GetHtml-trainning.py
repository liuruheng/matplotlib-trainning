#coding=utf-8
import urllib

#调用urllib模块
def getHtml(url):
    page = urllib.urlopen(url)
    html_training = page.read()
    urllib.urlretrieve(url,'d://XAG.html')
    return html_training

html_content = getHtml("http://finance.sina.com.cn/futures/quotes/XAG.shtml")
#html_content = getHtml("http://finance.sina.com.cn/nmetal/")
#html_content = getHtml("https://cdn.jin10.com/assets/js/index.js?20170928")
print html_content
