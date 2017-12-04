# -*- coding:utf8 -*-
import sqlite3
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from matplotlib.dates import MinuteLocator,HourLocator,DayLocator,DateLocator,DateFormatter,WeekdayLocator,MONDAY
from matplotlib.dates import datestr2num,strpdate2num,date2num
import numpy as np
import datetime
import inspect
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
import matplotlib.ticker as ticker

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
    listwithoutid = []
    for itemline in ret:
        clearline = []
        clearline.extend(itemline[1:])
        listwithoutid.append(clearline)
    #print ret
    #print listwithoutid
    # 抬头信息
    title = map(lambda x:x , ('time','open','high','low','close'))

    dataframe = DataFrame(listwithoutid,columns=title)
    #dataframe = DataFrame(ret)
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
    fig,ax = plt.subplots(figsize=(15,5))
    ax.xaxis.set_major_locator(HourLocator(interval=4))
    ax.xaxis.set_major_formatter(DateFormatter('%H'))
    #ax.xaxis.set_minor_locator(MinuteLocator(30))
    ax.grid(True)
    #axes = plt.subplot(111)
    #axes.set_ylim(16,18)
    data_list = []
    quotes = np.array(translate_db_to_df('D:\\misc\\future\\2017-47\\1day.db',-1))
    for q in quotes:
        #print q
        q[4] = datetime.datetime.strptime(q[4],"%Y-%m-%d %H:%M:%S")
        q[4] = date2num(q[4])
        data = (q[4],q[0],q[1],q[2],q[3])
        data_list.append(data)
    print data_list
    mpf.candlestick_ohlc(ax,quotes,width=0.4,colorup='g', colordown='r', alpha=1.0)
    ax.xaxis_date()

    #plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()

def sample_candlestick():
    # 设置历史数据区间
    date1 = (2014, 12, 1) # 起始日期，格式：(年，月，日)元组
    date2 = (2016, 12, 1)  # 结束日期，格式：(年，月，日)元组

    # 从雅虎财经中获取股票代码601558的历史行情
    #quotes = mpf.quotes_historical_yahoo_ohlc('601558.ss', date1, date2)
    stock_array = np.array(translate_db_to_df('D:\\misc\\future\\2017-48\\5min.db',50))
    quotes = stock_array
    #quotes = np.array(stock_array.reset_index()[['time','open','high','low','close']])
    #quotes[:,0] = strpdate2num(quotes[:,0])
    #print type(quotes)
    for q in quotes:
        print q
        q[0] = datetime.datetime.strptime(q[0],"%Y-%m-%d %H:%M:%S")
        q[0] = date2num(q[0])
        t, open, high, low,close = q[:5]
    #print type(datetime.datetime.now())
    #print date2num(datetime.datetime.now())
    # 创建一个子图
    fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
    fig.subplots_adjust(bottom=0.2)
    # 设置X轴刻度为日期时间
    #ax.xaxis_date()
    # X轴刻度文字倾斜45度
    plt.xticks(rotation=45)
    plt.title("stock code")
    plt.xlabel("time")
    plt.ylabel("price")
    mpf.candlestick_ohlc(ax,quotes,width=1.2,colorup='r',colordown='green')
    plt.grid(True)
    #plt.show()
    #print '%s'%(inspect.stack())

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def test_pyplot():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(10)
    plt.subplot(2,1,1)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r')

    #plt.subplot(212)
    #plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()

def sample_show():
    # (Year, month, day) tuples suffice as args for quotes_historical_yahoo
    date1 = (2004, 2, 3)
    date2 = (2004, 4, 12)

    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12
    quotes = []
    #quotes = quotes_historical_yahoo_ohlc('INTC', date1, date2)
    print matplotlib.dates.date2num(datetime.datetime(2004, 02, 9, 11, 02, 35))

    #day = datetime.datetime.strptime('2014-09-09', "%Y-%m-%d")
    #print day.strftime('%d')
    #kk = int(day.strftime('%d'))
    quotes = [(731613.0, 21, 21.9, 21.41, 21.49), \
    (731614.0, 21.58059381723535, 22.282458652866239, 21.495518496815286, 22.261189999999999, 62375400.0),\
    (731615.0, 21.970149977014657, 22.005642238507662, 21.302881405729515, 21.309979999999999, 79361900.0),\
    (731616.0, 21.544233552807487, 21.608121610928944, 21.118317897727273, 21.238994000000002, 74618700.0),\
    (731617.0, 21.331275659352869, 21.96305198651266, 21.288684802418548, 21.920459000000001, 55401000.0),\
    (731620.0, 22.076628501799149, 22.076628501799149, 21.636515650637879, 21.700403000000001, 36540300.0),\
    (731621.0, 21.778487611706364, 21.941755282850185, 21.530036807791852, 21.679107999999999, 36344100.0),\
    (731622.0, 21.91336157723601, 22.119220104549854, 21.672009368136301, 21.998543999999999, 52150100.0),\
    (731623.0, 21.970150190991514, 22.275388327876421, 21.806881101461325, 21.821079000000001, 38205500.0),\
    (731624.0, 22.00564283363115, 22.140516838277367, 21.196403774769969, 21.395163, 63292500.0),\
    (731628.0, 21.565529435727374, 21.927557756143742, 21.444853328921916, 21.870768999999999, 40220700.0),\
    (731629.0, 21.892065266666666, 21.977247690140558, 21.679108143192778, 21.721699000000001, 42232600.0),\
    (731630.0, 21.96305183341418, 22.076628634213069, 21.189304332194862, 21.217697999999999, 60100700.0),\
    (731631.0, 21.359670349000002, 21.366768943333334, 20.940853283333333, 21.295783, 70620300.0),\
    (731634.0, 21.288683819655173, 21.31707890606631, 20.337472205172414, 20.585923000000001, 92175800.0),\
    (731635.0, 20.443950809183328, 20.891162958521814, 20.42265573621042, 20.727896000000001, 68433000.0),\
    (731636.0, 20.891162998610298, 21.132515204506578, 20.798880562966996, 21.026036999999999, 54661900.0),\
    (731637.0, 20.969248086808577, 21.203501696639083, 20.834374086440679, 20.940853000000001, 45906300.0),\
    (731638.0, 21.082825713872271, 21.104120786845179, 20.65690934736612, 20.727896000000001, 58987700.0),\
    (731641.0, 20.614318374584329, 21.118317855563564, 20.479444374218783, 21.075727000000001, 65372800.0),\
    (731642.0, 21.118317913851349, 21.395162380005438, 20.983443913113547, 21.011838999999998, 65223700.0),\
    (731643.0, 20.983444491812552, 21.054431146197274, 20.47234640109, 20.614318999999998, 68249000.0),\
    (731644.0, 20.635613532546376, 21.08282568119164, 20.621415634154065, 21.047332000000001, 60135800.0),\
    (731645.0, 20.557528174509184, 20.855669132086355, 20.422655594036076, 20.550431, 118682400.0),\
    (731648.0, 20.628514408966737, 20.656909496140454, 19.606318245371433, 19.663107, 105763200.0),\
    (731649.0, 19.698599329878487, 19.947050132237315, 19.53533165975697, 19.861867, 92538800.0),\
    (731650.0, 19.904459821703437, 20.05352959734638, 19.28688138619119, 19.386261000000001, 88033100.0),\
    (731651.0, 19.230091594165437, 19.726993895605357, 19.194599333197676, 19.222992999999999, 97958600.0),\
    (731652.0, 19.521134000681329, 19.684401666868848, 19.421754391991826, 19.656008, 56526800.0),\
    (731655.0, 19.570824939852397, 19.585022128782285, 19.187501548604832, 19.237190999999999, 54857000.0),\
    (731656.0, 19.393359508100151, 19.528232798969075, 18.967443142865172, 19.279782000000001, 67306500.0),\
    (731657.0, 19.478543202894954, 19.805077826373594, 19.400457956802519, 19.726994000000001, 55548300.0),\
    (731658.0, 19.691500378253661, 19.741189827964458, 19.244289651981152, 19.308177000000001, 70686100.0),\
    (731659.0, 19.201696564583767, 19.428852998270138, 18.726090754089242, 18.804175999999998, 83734500.0),\
    (731662.0, 18.64090878307282, 18.80417645329775, 18.477641822707319, 18.619613000000001, 73006200.0),\
    (731663.0, 18.811275210244649, 18.953247808483294, 18.527331433486239, 18.569922999999999, 70217700.0),\
    (731664.0, 18.612513161512094, 19.073923201230599, 18.569922306448465, 18.832571000000002, 69501200.0),\
    (731665.0, 19.095218406073464, 19.73409117448416, 19.066824739120882, 19.726994000000001, 84754400.0),\
    (731666.0, 19.719896199263957, 19.769585650824894, 19.393360142927687, 19.435950999999999, 65644100.0),\
    (731669.0, 19.627612913412317, 19.840571448733716, 19.521134000681329, 19.656008, 66249300.0),\
    (731670.0, 19.471444000000002, 19.549529246498142, 19.237190390083853, 19.471444000000002, 62191000.0),\
    (731671.0, 19.464345363075541, 19.499837624337701, 19.180401594102882, 19.308177000000001, 57809100.0),\
    (731672.0, 19.428853825230266, 19.719896199263957, 19.364966474832631, 19.435950999999999, 55051700.0),\
    (731673.0, 19.876064158034705, 19.961248000000001, 19.627613356059271, 19.961248000000001, 78672000.0),\
    (731676.0, 20.089021142645713, 20.273584594294171, 19.961247865069485, 20.266486, 47534500.0),\
    (731677.0, 20.053528811460914, 20.195501406711216, 19.904459041659923, 20.067726, 70147800.0),\
    (731678.0, 19.932852625168263, 19.968344886507502, 19.506936970784327, 19.606318000000002, 72680200.0),\
    (731679.0, 19.932852477425921, 19.97544333268921, 19.308176898819003, 19.428853, 71791400.0),\
    (731683.0, 19.663107655511631, 19.712797107608694, 19.329473001086956, 19.592120999999999, 51016700.0)]
    #quotes = [(matplotlib.dates.date2num(datetime.datetime(2004, 02, 03)),32,43,23,33),(matplotlib.dates.date2num(datetime.datetime(2004, 02, 04)),32,43,23,36),(matplotlib.dates.date2num(datetime.datetime(2004, 02, 07)),52,45,23,33) ,(matplotlib.dates.date2num(datetime.datetime(2004, 02, 8)),52,45,23,33) ]
    #quotes.append((matplotlib.dates.date2num(datetime.datetime(2004, 2, 3)),32,43,23,33))
    #quotes.append((matplotlib.dates.date2num(datetime.datetime(2004, 2, 04)),42,65,33,43))
    #quotes.append((matplotlib.dates.date2num(datetime.datetime(2004, 2, 5)),33.0,63,23,53))
    #quotes.append((matplotlib.dates.date2num(datetime.datetime(2004, 2, 6)),34.34,43.343,23.34,33.34))
    #quotes.append((matplotlib.dates.date2num(datetime.datetime(2004, 2, kk)),32.34,43.34,23.3,33.3))

    #print quotes
    if len(quotes) == 0:
        raise SystemExit

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.xaxis.set_minor_formatter(dayFormatter)

    #plot_day_summary(ax, quotes, ticksize=3)
    candlestick_ohlc(ax, quotes, width=0.6)
    ax.grid(True)
    #ax.xaxis_date()
    #ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()

def six_hour_format_func(x,pos):
    return pos

def hour_trainning_show():
    quotes = [(731613.0, 21, 21.9, 21.41, 21.49), \
    (731613.1, 21.58059381723535, 22.282458652866239, 21.495518496815286, 22.261189999999999, 62375400.0),\
    (731613.2, 21.970149977014657, 22.005642238507662, 21.302881405729515, 21.309979999999999, 79361900.0),\
    (731613.3, 19.932852625168263, 19.968344886507502, 19.506936970784327, 19.606318000000002, 72680200.0),\
    (731613.4, 19.932852477425921, 19.97544333268921, 19.308176898819003, 19.428853, 71791400.0),\
    (731613.5, 19.663107655511631, 19.712797107608694, 19.329473001086956, 19.592120999999999, 51016700.0)]

    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%H')      # e.g., 12

    hourloc = HourLocator(interval=1)
    minloc = MinuteLocator(interval=30)

    fig, ax = plt.subplots(figsize=(8,5))
    fig.subplots_adjust(bottom=0.2)
    #ax.xaxis.set_major_locator(mondays)
    #ax.xaxis.set_minor_locator(alldays)
    #ax.xaxis.set_major_formatter(weekFormatter)
    #ax.xaxis.set_minor_formatter(dayFormatter)
    ax.xaxis.set_major_locator(minloc)
    ax.xaxis.set_major_formatter(DateFormatter('%M'))

    #plot_day_summary(ax, quotes, ticksize=3)
    candlestick_ohlc(ax, quotes,width=0.01)
    ax.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()

if __name__ == '__main__':
    #drawing_figure()
    #drawing_candlestick()
    #sample_candlestick()
    #test_pyplot()
    #sample_show()
    hour_trainning_show()
