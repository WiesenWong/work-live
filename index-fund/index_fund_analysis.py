# coding=utf-8
from datetime import datetime
import requests as rs
import requests
import matplotlib.pyplot as plt
import json
import random
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STXINWEI.TTF')

def timestamp2datetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def getUrl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response = rs.get(url,headers=headers)
    data = json.loads(response.text)
    return data

def showPic(codelist):
    #519671
    length = 0
    plt.figure(figsize=(25, 15))
    for code in codelist:
        colors = (random.uniform(0.1,1),random.uniform(0.1,1),random.uniform(0.1,1))
        data = getUrl('https://danjuanapp.com/djapi/fund/estimate-nav/' + code)['data']
        details = getUrl('https://danjuanapp.com/djapi/fund/' + code)['data']
        plt.plot(getdata(data,'time'),getdata(data,'percentage'),label=details['fd_name'],color=colors)
        length = len(getdata(data,'time'))
    
    plt.legend(prop=myfont,fontsize=30)
    xlabel = []
    i = 0
    while i <= length:
        xlabel.append(i)
        i = i + 30
    plt.xticks(xlabel)
    plt.show()

def getdata(data,xtype = 'time'):
    a = []
    for item in data['items']:
        if xtype == 'time':
            a.append(timestamp2datetime(item['time']/1000).strftime('%H:%M'))
        else:
            a.append(item[xtype])
    return a
    
if __name__ == '__main__':
    codelist= ['519671','000968','090010','530015']
    showPic(codelist)
    codelist= ['003318','001548','070023','160632','001594']
    showPic(codelist)