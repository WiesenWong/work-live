# coding=utf-8
from datetime import datetime
import requests as rs
import requests
import matplotlib.pyplot as plt
import json
import random

BASE_HEADLINE = '螺丝钉定投实盘'

def getDateTime():
    #获取当前时间
    _date = datetime.now()
    print('current time: %s' % (format(_date.strftime('%Y-%m-%d %H:%M:%S'))))
    return _date

def getHeadLind(date):
    return BASE_HEADLINE + '｜第 '+ timestamp2datetime(date).strftime('%Y-%m-%d') +' 期'

def timestamp2datetime(timestamp):
    return datetime.fromtimestamp(timestamp)
   
def getUrl(url):
    #获取最新一期螺丝钉定投实盘
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response = rs.get(url,headers=headers)
    data = json.loads(response.text)
    return data

def getInvestor(trading_elements,headLind,investmentAmount = 10000):
    total = 0
    print()
    print(headLind)
    print('------------------------------------------------------------')
    #print('Please enter your investment amount')
    #investmentAmount = input()
    for item in trading_elements:
        total += item['money']
    for item in trading_elements:
        print('name: ' + item['fd_name'])
        print('code: ' + item['fd_code'])
        print('investmentAmount: ' + str(round(float(investmentAmount) * item['portion'])))
        print('------------------------------------------------------------')

def showPic(codelist):
    #519671
    for code in codelist:
        colors = (random.randint(0,1),random.randint(0,1),random.randint(0,1))
        url = 'https://danjuanapp.com/djapi/fund/estimate-nav/'+ code
        data = getUrl(url)['data']
        plt.plot(getdata(data,'time'),getdata(data,'percentage'),color=colors)
    plt.show()
    return 0

def getdata(data,xtype = 'time'):
    a = []
    for item in data['items']:
        if xtype == 'time':
            a.append(timestamp2datetime(item['time']/1000).strftime('%H:%M'))
        else:
            a.append(item[xtype])
    return a
def getcodelist(trading_elements):
    a = []
    for item in trading_elements:
        a.append(item['fd_code'])
    return a    
if __name__ == '__main__':
    print('Welcome to use the system of index fund')
    investmentAmount = 4000
    getDateTime()
    url = 'https://danjuanapp.com/djapi/plan/CSI666/trade_history?size=1&page=1'
    data = getUrl(url)['data']['items'][0]
    headLind = getHeadLind(float(data['trade_date'])/1000)
    codelist = getcodelist(data['trading_elements'])
    #showPic(codelist)
    getInvestor(data['trading_elements'],headLind,investmentAmount)
    