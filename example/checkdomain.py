#!/usr/bin/env python
# encoding: utf-8
#by luwen
import re
import sys
import time
import json
import urllib
import urllib2
import smtplib
import datetime
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


def get_domain(reqUrl,key,reqDomain):
    reqUrl = reqUrl
    data = {'key': key,'host': reqDomain}
    #构造数据格式
    postData = urllib.urlencode(data)
    req = urllib2.Request(reqUrl,postData)
    #解析json
    msg = json.load(urllib2.urlopen(req))
    return msg

if __name__ == "__main__":
    #发送邮件参数
    from_addr = '****@**.com'
    #to_addr = ['jk@jf.com','luwen@jf.com']
    to_addr = ['****@**.com']
    password = '******'
    smtpServer = 'smtp.**.com'
    #请求查询域名信息参数
    url = 'http://api.91cha.com/whois'
    key = '**************************'
    #今天日期
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    #格式化今天日期
    todayStr = datetime.datetime.strptime(today,'%Y-%M-%d')
    with open('domaintest.txt') as file:
        for domain in file:
            host = domain.strip('\n')
            msgHost  = get_domain(url,key,host)
            #判断查询是否成功
            if msgHost['state'] != 1:
                errorCode = msgHost['state']
                subject = '%s域名查询出错' %host
                content = "%s域名查询出错，错误代码%s,请检查\n" %(host,errorCode)
                to_addr = ['****@**.com']
                sendmail(from_addr,password,to_addr,smtpServer,subject,content)
                time.sleep(10)
                continue
            #到期日期
            expired = msgHost['data']['expiretime']
            #格式化到期日期
            expiredStr = datetime.datetime.strptime(expired,'%Y-%M-%d')
            #剩余时间
            periodTime = (expiredStr - todayStr).days
            if periodTime < 300:
                subject = '%s域名即将过期提醒邮件' %host
                content = "%s域名还有%s天过期，请注意续费\n" %(host,periodTime)
                sendmail(from_addr,password,to_addr,smtpServer,subject,content)
                time.sleep(10)
