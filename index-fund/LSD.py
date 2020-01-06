# coding=utf-8
from datetime import datetime
import requests as rs
import requests
import json

BASE_HEADLINE = '螺丝钉定投实盘'

def getDateTime():
    #获取当前时间
    _date = datetime.now()
    print('current time: %s' % (format(_date.strftime('%Y-%m-%d %H:%M:%S'))))
    return _date

def getHeadLind(date):
    return BASE_HEADLINE + '｜第 '+ datetime.fromtimestamp(date).strftime('%Y-%m-%d') +' 期'
    
def getUrl():
    #获取最新一期螺丝钉定投实盘
    url = 'https://danjuanapp.com/djapi/plan/CSI666/trade_history?size=1&page=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response = rs.get(url,headers=headers)
    d = json.loads(response.text)
    return d['data']['items'][0]

def getInvestor(trading_elements,investmentAmount = 10000):
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
        
if __name__ == '__main__':
    print('Welcome to use the system of index fund')
    investmentAmount = 1000
    getDateTime()
    data = getUrl()
    headLind = getHeadLind(float(data['trade_date'])/1000)
    getInvestor(data['trading_elements'],investmentAmount)
    