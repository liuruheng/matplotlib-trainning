# -*- coding:utf8 -*-
import sqlite3
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from matplotlib.dates import MinuteLocator,HourLocator,DateLocator,DateFormatter


def translate_db_to_df(dbFile, lineCnt):
    """ 外部接口API: 将db文件中的条目转换成dateframe格式
        dbFile: db文件名（含文件路径）
        lineCnt: 截取db条目数目。注：‘-1’表示全部转换。
    """
    ret = None
    # db文件操作
    db = sqlite3.connect(dbFile)
    dbCursor = db.cursor()
    try:
        results = dbCursor.execute('select * from quotation order by id')# 倒序方式查询
        if lineCnt == -1: # 获取所有条目
            ret = results.fetchall()
        else:# 获取指定数量的最近条目
            ret = results.fetchmany(lineCnt)
    except (Exception),e:
        print "fatal", " translate quotation Exception: " + e.message
    finally:
        dbCursor.close()
        db.close()
        if ret == None: return None

    # 抬头信息
    title = ['id'] + map(lambda x:x , ('open','high','low','close','time'))

    dataframe = DataFrame(ret,columns=title)
    return dataframe

def drawing_figure():
    x_values=list(range(1,101))
    y_values=[x**2 for x in x_values]

    #必须放在scatter语句之前
    #中文注释需要增加第一行编码格式说明
    plt.figure(figsize=(8, 6))

    plt.scatter(x_values, y_values, edgecolor='blue', c='green', s=1)

    plt.title("Square Numbers", fontsize=10)
    plt.xlabel("Value", fontsize=10)
    plt.ylabel("Square of Value", fontsize=10)

    #plt.tick_params(axis="both",which='major', width=1, labelsize=10)

    plt.axis([0, 101, 0, 10010])

    plt.show()

def drawing_candlestick():
    hourlocator = HourLocator()

    fig,ax = plt.subplots()
    ax.xaxis.set_major_locator(MinuteLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%M'))
    ax.grid(True)

    stock_array = translate_db_to_df('D:\\misc\\future\\2017-48\\15min.db',20)
    quotes = stock_array.ix[:,[5,1,2,3,4]]
    print type(quotes)
    #mpf.candlestick_ohlc(ax,stock_array)

def sample_candlestick():
    # 设置历史数据区间
    date1 = (2014, 12, 1) # 起始日期，格式：(年，月，日)元组
    date2 = (2016, 12, 1)  # 结束日期，格式：(年，月，日)元组
    # 从雅虎财经中获取股票代码601558的历史行情
    quotes = mpf.quotes_historical_yahoo_ohlc('601558.ss', date1, date2)

    # 创建一个子图
    fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
    fig.subplots_adjust(bottom=0.2)
    # 设置X轴刻度为日期时间
    ax.xaxis_date()
    # X轴刻度文字倾斜45度
    plt.xticks(rotation=45)
    plt.title("股票代码：601558两年K线图")
    plt.xlabel("时间")
    plt.ylabel("股价（元）")
    mpf.candlestick_ohlc(ax,quotes,width=1.2,colorup='r',colordown='green')
    plt.grid(True)

if __name__ == '__main__':
    #drawing_figure()
    drawing_candlestick()
    #sample_candlestick()
