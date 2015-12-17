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
#import os
import urlparse
import linecache
import url_config
import user_config

baseurl = url_config.lb_url
apikey = user_config.apikey
secretkey = user_config.secretkey

lbname=''	# lb name

if apikey != "":
	request={}
	request['command']='createLoadBalancer'
	request['zoneid']='eceb5d65-6571-4696-875f-5a17949f3317'
	request['name']=lbname
	request['loadbalanceroption']='roundrobin'
	request['serviceport']='80'
	request['servicetype']='http'
	request['healthchecktype']='tcp'
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print "apikey none"