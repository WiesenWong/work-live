# coding=utf-8
from datetime import datetime
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import requests
import math
import string

BASE_URL = 'http://weixin.sogou.com'
BASE_NUM = 91
BASE_DATE = '2019-10-22 23:59:59'
BASE_HEADLINE = '螺丝钉定投实盘'
BASE_FUND = [
 {
	'name' : '300价值',
	'code' : '519671',
	'num' : 2289
 },
  {
	'name' : '中证红利',
	'code' : '090010',
	'num' : 2251
 },
 {
	'name' : '基本面60',
	'code' : '530015',
	'num' : 1846
 },
 {
	'name' : '香港中小',
	'code' : '501021',
	'num' : 1714
 },
 {
	'name' : '500低波动',
	'code' : '003318',
	'num' : 2155
 },
 {
	'name' : '养老产业',
	'code' : '000968',
	'num' : 1732
 }
]
def getDateTime():
	#获取当前时间
	_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print('current time: %s' % (format(_date)))
	return _date
def getNum():
	currentTime = datetime.strptime(getDateTime(),'%Y-%m-%d %H:%M:%S')
	baseTime = datetime.strptime(BASE_DATE,'%Y-%m-%d %H:%M:%S')
	interval = currentTime - baseTime
	num = interval.total_seconds()/(3600*24*7)
	#向下取整
	floorNum = math.floor(num)
	num = floorNum + BASE_NUM
	return num
def getHeadLind():
	return BASE_HEADLINE + '｜第' + str(getNum()) + '期'
	
def getUrl():
	#获取最新一期螺丝钉定投实盘
	#https://weixin.sogou.com/weixin?type=2&query=%E8%9E%BA%E4%B8%9D%E9%92%89%E5%AE%9A%E6%8A%95%E5%AE%9E%E7%9B%98%EF%BD%9C%E7%AC%AC91%E6%9C%9F&ie=utf8&s_from=input&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=1&sourceid=sugg&sut=0&sst0=1571798127563&lkt=0%2C0%2C0&p=40040108
	sogoUrl = BASE_URL + '/weixin?type=2&query=' + getHeadLind() + '&ie=utf8&s_from=input&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=1&sourceid=sugg&sut=0&sst0=1571798127563&lkt=0%2C0%2C0&p=40040108'
	data = urlopen(quote('', safe=string.printable))
	dom = BeautifulSoup(data,'html.parser')
	return dom

def getInvestor():
	total = 0
	print('Please enter your investment amount')
	investmentAmount = input()
	for one in BASE_FUND:
		total += one['num']
	print(total)
	
	for one in BASE_FUND:
		print('name: ' + one['name'])
		print('code: ' + one['code'])
		print('investmentAmount: ' + str(round(float(investmentAmount) * one['num'] / total)))
		print('------------------------------------------------------------')
		
if __name__ == '__main__':
	print('Welcome to use the system of index fund')
	getDateTime()
	data = urlopen(quote('https://mp.weixin.qq.com/s?src=11&timestamp=1571798253&ver=1929&signature=FOSQbRqM-KWLnxZ3yjXHqc6RwmSm*cssdYygrSbgIUBC4aEFA8YM8i3kcLq9rT6qvPTUPjmJYCTpJOcLGmmyo3DTn27*AQZzX4ttZCjCqdu3xnwpGmPaZwvP09Z1nxNs&new=1', safe=string.printable))
	dom = BeautifulSoup(data,'html.parser')
	print(dom)
	getHeadLind()
	getInvestor()
	
	