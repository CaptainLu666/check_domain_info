#!/usr/bin/env python
# encoding: utf-8
#by luwen
import bs4
import re
import sys
import time
import json
import urllib
import urllib2
import smtplib
import datetime
import requests
from email.mime.text import MIMEText
from email.header import Header

def sendmail(from_addr,password,to_addr,smtpServer,subject,content):
    from_addr = from_addr
    password = password
    to_addr = to_addr
    smtp_server = smtpServer
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = from_addr
    msg['To'] = ','.join(to_addr)
    msg['Subject'] = subject
    server = smtplib.SMTP(smtp_server,25)
    #server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()


def get_domain(reqUrl,reqDomain):
    reqUrl = reqUrl
    data = {'DomainName':reqDomain,'isforceupdate':1}
    #构造数据格式
    req_raw = requests.get(reqUrl, params=data)
    soup = bs4.BeautifulSoup(req_raw.text,"lxml")
    #print soup.prettify()
    #response = soup(class_='fr WhLeList-right')
    res_msg = soup.get_text().encode("utf-8")
    #req = json.dumps(req_raw.json())
    #解析json
    #msg = json.loads(req)
    return res_msg

if __name__ == "__main__":
    #发送邮件参数
    from_addr = '****@**.com'
    to_addr = ['jk@**.com']
    #to_addr = ['luwen@jf.com']
    password = '*******'
    smtpServer = 'smtp.**.com'
    #请求查询域名信息参数
    reqUrl = 'http://whois.chinaz.com'
    #今天日期
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    todayStr = today.split('-')
    #格式化今天日期
    #todayStr = datetime.datetime.strptime(today,'%Y-%M-%d')
    d1 = datetime.datetime(int(todayStr[0]), int(todayStr[1]), int(todayStr[2]))
    #pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
    #pattern = re.compile(r"(\d{4})年(\d{2})月(\d{2})日")
    res = r'过期时间(\d{4})年(\d{2})月(\d{2})日'
    with open('domain.txt') as file:
        for domain in file:
            host = domain.strip('\n')
            try:
                msgHost = get_domain(reqUrl,host)
            except Exception,e:
                print Exception,":",e
                continue
            #判断查询是否成功
            #if msgHost['state'] != 1:
            #    errorCode = msgHost['state']
            #    subject = '%s域名查询出错' %host
            #    content = "%s域名查询出错，错误代码%s,请检查\n" %(host,errorCode)
            #    to_addr = ['luwen@jf.com']
            #    sendmail(from_addr,password,to_addr,smtpServer,subject,content)
            #    time.sleep(10)
            #    continue
            #到期日期
            print host
            try:
                expired_raw = re.search(res,msgHost)
                #expired_raw = pattern.match(msgHost)
            except Exception,e:
                print Exception,":",e
                continue


            #格式化到期日期
            #expiredStr = expired.split('-')
            #d2 = datetime.datetime(int(expiredStr[0]), int(expiredStr[1]), int(expiredStr[2]))
            try :
                d2 = datetime.datetime(int(expired_raw.group(1)), int(expired_raw.group(2)), int(expired_raw.group(3)))
            except Exception,e:
                print Exception,":",e
                subject = '%s域名查询出错' %host
                content = "%s域名查询过期时间出错，请注意检查\n" %(host)
                sendmail(from_addr,password,to_addr,smtpServer,subject,content)
                continue
            #剩余时间
            periodTime = (d2 - d1).days
            print periodTime
            if periodTime < 60:
                subject = '%s域名即将过期提醒邮件' %host
                content = "%s域名还有%s天过期，请注意续费\n" %(host,periodTime)
                sendmail(from_addr,password,to_addr,smtpServer,subject,content)
                time.sleep(10)
