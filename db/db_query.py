#!/usr/bin/python

import sys
sys.path.insert(0, "../config/")
sys.path.insert(0, "../ucloudbiz/")
import ucloudbiz
import urllib2
import urllib
import hashlib
import hmac
import base64
import urlparse
import linecache
import url_config
import ast

fabricurl=url_config.fabric_url

hagroupname='edu_ucloudbiz_XX_hagroup!'
sec='1'			# 1 (public access), 0 (private access)
mode='3'		# 2 (Read mode), 3 (Read/Write mode)

finalurl = fabricurl + 'grpcode=' + hagroupname + "&sec=" + sec + "&mode=" + mode
res=urllib2.urlopen(finalurl)
codes = res.read().replace('\u0000','').replace('null','').replace('(', '').replace(')', '')
result=ast.literal_eval(codes)
lst=result['code'].split(':')
res.close()

import MySQLdb as mdb
import sys

hostip=lst[0]
portno=int(lst[1])
username='root'
password='admin12345'
database='sakila'
sql="select title, release_year from film limit 5"

print
print "Host IP = %s" % hostip
print "Host Port = %s" % portno
print

con = mdb.connect(host=hostip, port=portno, user=username, passwd=password, db=database);
cur = con.cursor()
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
	print row
con.close()
print
