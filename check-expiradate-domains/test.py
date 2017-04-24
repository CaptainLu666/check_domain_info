#!/usr/bin/env python
# encoding: utf-8
import re
import urllib
import urllib2
import json
import requests
#from lxml import html
import bs4
import datetime

#data = {'domainName':'luwen.com','username':'mikeluwen','password':'luwenlin901122','outputFormat':'JSON'}
#reqUrl = 'https://www.whoisxmlapi.com/whoisserver/WhoisService'
#r = requests.get(reqUrl, params=data)
#b = json.dumps(r.json())
#a = json.loads(b)
#d = a['WhoisRecord']['expiresDate']
#pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
#print pattern.match(d).group(0)

#postData = urllib.urlencode(data)
#req = urllib2.Request(reqUrl,postData)
#response = urllib2.urlopen(req)
#print response.read()

#key='**************8'
#secret_key='LSJDLJLJDSLJFLJSLFJLSJFLSJDLFJLKJ********************'

data = {'DomainName':'baidu.com'}
reqUrl = 'http://whois.chinaz.com'
r = requests.get(reqUrl, params=data)
#pattern = re.compile(r"(\d{4})年(\d{2})月(\d{2})日")
#pattern = re.compile(r'(\d{4})年(\d{2})月(\d{2})日')
#pattern = re.compile(r"(\d{4})[\u2e80-\u4dfh](\d{2})[\u2e80-\u4dfh](\d{2})[\u2e80-\u4dfh]")
#res1 = ur'<span>(\d{4}[\u2e80-\u4dfh]\d{2}[\u2e80-\u4dfh]\d{2}[\u2e80-\u4dfh])</span>'
res = r'过期时间(\d{4})年(\d{2})月(\d{2})日'

#res1= r'\d{4}[\u2e80-\u4dfh]\d{2}[\u2e80-\u4dfh]\d{2}[\u2e80-\u4dfh]'

#mike = re.findall(res1,data,re.S|re.M)
#mike = re.findall(res1,data)
#for i in mike:
#    print i
#pattern2 = re.compile(r"(\d{4})年(\d{2})月(\d{2})日")
#pattern2 = re.compile(r"(\d{2})")
#res_tr=r'<span>(.*?)</span>'
#res_tr=r'<span>(.*?)</span>'
#m_tr = re.findall(res_tr,data,re.S|re.M)
#for m in m_tr:
#    print m
#pattern2 = re.compile(r"<div class="fl WhLeList-left">过期时间</div><div class="fr WhLeList-right"><span>(\d{4})年(\d{2})月(\d{2})日</span></div>")
#mike = pattern2.match(data)
#<span>2017年11月20日</span>
#r = re.findall(r"(\d{4})年",data)
#print r
#for url in r:
#    print url


soup = bs4.BeautifulSoup(r.text,"lxml")
#context = soup.find('ul', class_='WhoisLeft fl',id="sh_info")
#context_ = context.find_all('li', class_="clearfix bor-b1s ")
#context__ = context.find_all('li', class_="clearfix bor-b1s ")
#print context_
#print soup.original_encoding
#print soup.prettify()
#print soup.li
#res = soup.find(class_='fr WhLeList-right').find('span').string
#print res

#response = soup(class_='fr WhLeList-right')
res_content = soup.get_text().encode("utf-8")
#print res_content
#a = re.search(r'(\d{4})年(\d{2})月(\d{2})日',res_content)
#b = pattern.match(res_content)
c = re.findall(res,res_content,re.S|re.M)
d = re.search(res,res_content)
print d.group(1) + '-' + d.group(2) + '-' + d.group(3)
#print c
#print a.groups()
#print response.span.string.encode('utf-8')

#expired_raw = pattern.match(response)
#print expired_raw

#response = soup.find_all(class_='fr WhLeList-right')
#print response
#response = soup(class_='clearfix bor-b1s bg-list')
#response = soup(class_='IcpMain02')
#for sp in response:
#    print sp.span

#for sp in response:
#    print sp
#if not response[4]:
#    print response[3].span.string
#else:
#    print response[4].span.string




#print response.find_all('span')
#expired_raw = response[4].span
#.string.encode('utf-8')
#c = datetime.datetime.strptime(expired_raw,'%b-%d-%y')
#print c

#expired = pattern.match(expired_raw)
#print expired.group(1) + '-' + expired.group(2) + '-' + expired.group(3)

#print expired
#for sp in res:
#        print sp.span
#print soup.find("div", class_='fr WhLeList-right').find("span").text

#a = "".join(soup.find_all('span'))
#print a.encode('utf-8')


#tree = html.fromstring(r.text)

#old_time = tree.xpath('//span[@class="fr WhLeList-right"]')
#print old_time

#/html/body/div[2]

#print req_whois.read().decode()
