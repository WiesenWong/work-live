# coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pymysql
import pandas as pd
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import matplotlib.dates as mdates
large = 500
med = 16
small = 12

params = {
            'legend.fontsize': med,
            'figure.figsize': (16, 10),
            'axes.labelsize': med,
            'axes.titlesize': med,
            'xtick.labelsize': med,
            'ytick.labelsize': med,
            'figure.titlesize': large}

plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STXINWEI.TTF')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#指定X轴的以日期格式（带小时）显示
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%m'))
def getDateFromDB(sql):
    db = pymysql.connect('127.0.0.1','root','Winson94','index_fund')
    cursor = db.cursor();
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data

def getDateFromCSV(path):
    data = pd.read_csv(path)
    return data

# Bsae function
def getlim(series):
    #series = np.sort(series, kind = 'heapsort')
    min_series = series[series.idxmin()]
    max_series = series[series.idxmax()]
    tenth_scale = (max_series - min_series) / 20.0
    return (min_series - tenth_scale,max_series + tenth_scale)


def showPic(data,xlabel,ylabel,categorie):
    categories = np.unique(data[categorie])
    print(len(categories))
    colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
    for i, item in enumerate(categories):
        plt.plot(xlabel, ylabel, data=data.loc[data[categorie]==item, :], c=colors[i], label=str(item))
    
    
    plt.gca().set(xlabel = xlabel, ylabel = ylabel)
    
    plt.legend(fontsize=12)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    #plt.title(title, fontsize=22)
    #plt.savefig(".//output//"+title+".png")
    plt.show()


#基金收益走势图
def showIncome(user,fundtype):
    print(0)
#基金走势图
def showPer(user,fundtype):
    sql = 'select fvh.code,fvh.nav,fvh.percentage,fvh.time from fund_value_his fvh left join fund_hold_info fhi on fhi.code = fvh.code where fvh.time > CURRENT_DATE() and fhi.fund_type = "'+ fundtype +'" and fhi.user = "'+ user +'"'
    data = pd.DataFrame(list(getDateFromDB(sql)))
    data.columns = ['code','nav','per','time']
    xlabel = 'time'
    ylabel = 'per'
    categorie = 'code'
    showPic(data,xlabel,ylabel,categorie)
if __name__ == '__main__':
    showPer('Winson','index_fund')
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    