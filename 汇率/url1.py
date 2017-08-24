#made by eric,2017/8/24
#coding=utf-8
import urllib
import re
import time
import os

def getKey(html,findkey):
    reg = findkey
    weatherList = re.findall(reg,html,re.S)
    return weatherList
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html

def getAnswer():
    f = open("/汇率/a1.txt",'w')
    #读网站
    hl = getHtml('http://www.bnm.gov.my/index.php?ch=statistic&pg=stats_exchangerates')
    #提取第一,二组汇率
    num = getKey(hl,"<tr class='TblHdr'>(.*?)<td>&nbsp;</td>")
    num =  num[0]
    num = getKey(num,'<td>(.*?)</td>')

    #提取汇率对应名称
    name = getKey(hl,'<b>(.*?)</b>')

    #打印数据时间
    f.write(num[-10]+'\n')

    #打印货币名称以及汇率
    m = 1
    n = -10
    for i in range(9) :
        f.write(name[m] + ' : ' + num[n+1]+'\n')
        #n + 1是因为n = -10是数据时间。
        #这里name[m]是因为m = 0是空行，不可以用i（i从0开始）。
        #这里num[n+1]使用负数索引，为了总是得到最新数据。
        n = n+1
        m = m+1
    f.close()
h = 0
while True :
    dt=list(time.localtime())
    if h == 0:
        getAnswer()
        fa = open("/汇率/log1.txt",'a')
        fa.write('url1,ok,time : '+str(dt[3])+':'+str(dt[4])+':'+str(dt[5])+'\n')
        fa.close()
        h = 1
    minute=dt[4]
    second = dt[5]
    if minute == 00 :
        if second == 00:
          os.system('clear')
          getAnswer()
          fa = open("/汇率/log1.txt",'a')
          fa.write('url1,ok,time : '+str(dt[3])+':'+str(dt[4])+':'+str(dt[5])+'\n')
          fa.close()
          
    else :
        time.sleep(1)


    
