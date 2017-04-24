#!/usr/bin/env python
# encoding: utf-8
#by luwen
import re
import sys
import time
import datetime
import pythonwhois
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendmail(to_addr,subjt,content):
    from_addr = '*****@**.com'
    password = '*****'
    to_addr = to_addr
    smtp_server = 'smtp.**.com'
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = from_addr
    msg['To'] = ','.join(to_addr)
    msg['Subject'] = subjt
    server = smtplib.SMTP(smtp_server,25)
    server.login(from_addr,password)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()
def daysdiff(d1,d2):
        daysec = 24 * 60 * 60
        return int(( d1 - d2 )/daysec)

with open('domain.txt') as file:
    for domain in file:
        domain_new = domain.strip('\n')
        try:
            expiration_time = str(pythonwhois.get_whois(domain_new)['expiration_date'][0])
        except:
            try:
            #    time.sleep(60)
                expiration_time = str(pythonwhois.get_whois(domain_new)['expiration_date'][0])
            except:
                subjt = "%s域名查询出错" %domain_new
                content = "%s域名查询过期时间出错，请排查原因" %domain_new
                to_addr = ['**@***.com']
                sendmail(to_addr,subjt,content)
                today = datetime.date.today()
                fdomain = open('checkdomain.log','a')
                error_content = "%s:  检查%s域名过期时间出错\n" %(today,domain_new)
                fdomain.write(error_content)
                fdomain.close()
            #    time.sleep(60)
                continue
        time.strptime(expiration_time,'%Y-%m-%d %H:%M:%S')
        expiration_unix_time = time.mktime(time.strptime(expiration_time,'%Y-%m-%d %H:%M:%S'))
        local_unix_time = time.mktime(datetime.datetime.now().timetuple())
#            time_diff = expiration_unix_time - local_unix_time
        time_diff = daysdiff(expiration_unix_time,local_unix_time)
#            print time_diff
        if time_diff < 60:
            subjt = '%s域名即将过期提醒邮件' %domain_new
            content = "%s域名还有%s天过期，请注意续费\n" %(domain_new,time_diff)
            to_addr = ['**@**.com']
            sendmail(to_addr,subjt,content)
            #time.sleep(60)
