# coding=utf-8
import datetime
import requests as rs
import requests
import matplotlib.pyplot as plt
import json
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STXINWEI.TTF')

base_fund_num = [
            3026.74,
            1441.76,
            2755.84,
            1283.00,
            4399.61,
            394.33,
            2403.86]

def timestamp2datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

def getUrl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response = rs.get(url,headers=headers)
    data = json.loads(response.text)
    return data

def showPic(codelist):
    #519671
    length = 0
    plt.figure(figsize=(16, 10))
    
    indexlist = []
    
    colors = [plt.cm.tab10(i/float(len(codelist) - 1)) for i in range(len(codelist))]
    for i,code in enumerate(codelist):
        data = getUrl('https://danjuanapp.com/djapi/fund/estimate-nav/' + code)['data']
        details = getUrl('https://danjuanapp.com/djapi/fund/' + code)['data']
        
        xvar = getdata(data,'time')
        yvar = getdata(data,'percentage')
        length = len(xvar)
        indexlist.append(getdata(data,'nav'))
        
        plt.plot(xvar,yvar,label=details['fd_name'] + '(' + str(yvar[length - 1]) + ')',color=colors[i])
        
        #timeit.timeit('getdata(data)', 'from __main__ import fun', number=1)
        #plt.text(xvar[length - 1], yvar[length - 1], yvar[length - 1], ha='center', va='bottom', fontsize=12,color=colors[i])
    plt.axhline(y=0,ls='--',c='gray')
    plt.legend(prop=myfont,fontsize=30,loc='upper left')
    
    xlabel = []
    i = 0
    while i <= length:
        xlabel.append(i)
        i = i + 10
    plt.xticks(xlabel)
    plt.show()
    return indexlist

def getdata(data,xtype = 'time'):
    a = []
    for item in data['items']:
        mintime = timestamp2datetime(data['date']/1000) + datetime.timedelta(minutes=690)
        if timestamp2datetime(item['time']/1000) == mintime:
            if xtype == 'time':
                a.append(timestamp2datetime(item['time']/1000).strftime('%H:%M'))
                i = 1
                while i < 90:
                    a.append((mintime + datetime.timedelta(minutes=i)).strftime('%H:%M'))
                    i = i + 10
            else:
                a.append(item[xtype])
                i = 1
                while i < 90:
                    a.append(None)
                    i = i + 10
        else:
            if xtype == 'time':
                a.append(timestamp2datetime(item['time']/1000).strftime('%H:%M'))
            else:
                a.append(item[xtype])
    return a
    
if __name__ == '__main__':
    codelist= [
            '519671',
            '000968',
            '090010',
            '530015',
            '003318',
            '070023',
            '001594'
            ]
    indexlist = showPic(codelist)
    print(indexlist)
    
    