# -*- coding: utf-8 -*-

import requests
import requests.packages.urllib3.util.ssl_
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
hea = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'} 
homepage_url = "https://www.baidu.com/s?wd=天杀的"
local_cookies = r'cookies.txt'
def getHomepage(url,cookie_jar):
    # cookiePath = 'cookies.txt'
    f=open(cookie_jar,'r') 
    cookies={} 
    for line in f.read().split(';'): 
        #其设置为1就会把字符串拆分成2份 
        name,value=line.strip().split('=',1) 
        cookies[name]=value
    res = requests.get(url,headers = hea,cookies=cookies,allow_redirects=False)
    if res.status_code == 302:
        location_url = res.headers['Location']
        print '页面重定向，可能是没登陆或token错误，可跳转到\n %s' % location_url
        getHomepage(location_url,local_cookies)
    elif res.status_code == 200:
        
        print '头信息:\n%s \n 内容:\n%s' %(res.headers,res.text)


def getRsaPwd():
    public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQComqoAyvbCqO1EGsADwfNTWFQIUbm8CLdeb9TgjGLcz95mAo204SqTYdSEUxFsOnPfROOTxhkhfjbRxBV4/xjS06Y+kkUdiMGFtABIxRQHQIh0LrVvEZQs4NrixxcPI+b1bpE0gO/GAFSNWm9ejhZGj7UnqiHphnSJAVQNz2lgowIDAQAB'


    return
getHomepage(homepage_url,local_cookies)