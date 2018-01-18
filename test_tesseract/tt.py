#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import pytesseract
from PIL import Image
import re
import webbrowser

sys.path.append("libs")
# reload(sys)   
# sys.setdefaultencoding('utf8')   


furl = 'https://www.baidu.com/s?wd='

def openurl(url):
	# url = 'https://www.baidu.com/s?wd=123'

	# webbrowser.encode('gbk').open_new(url)
	webbrowser.open(url)
	# print webbrowser.get()


def getstr(imagepath):
	
	image = Image.open(imagepath)
	code = pytesseract.image_to_string(image,lang='chi_sim')
	# res = re.search(r'^[0-9]+\..*\n', code)

	# 将正则表达式编译成Pattern对象
	# pattern = re.compile(r'^[0-9]+\..*')
	res = re.search(r'[0-9]+\..*\?', code,re.DOTALL)

	# if (res != None )& (len(res)==1 ):	
	# 	print '\n\n','抓取结果1：\n',res[0]
	if res :
		# print '\n','抓取结果：\n',res.group(),'\n'
		return res.group()

	else:
		# print '\n','抓取结果：\n','无匹配结果','\n'
		return None

# s="中文" 
# def isUnicoded(s):
	
# 	if isinstance(s, unicode): 
# 	#s=u"中文" 
# 		print '1' 
# 		return s.encode('gbk') 
# 	else: 
# 	#s="中文" 
# 		print '2'
# 		return s.decode('utf-8').encode('gb2312')



ans = getstr('testt/12.png')
if ans :
	print '\n','抓取结果：\n',ans,'\n'
	urlstr = furl+ans

	# urlstr = 'https://www.baidu.com/s?wd=%s'% ans
	print 'url:',urlstr,(urlstr.encode('utf8'),)

	openurl(urlstr)
	# openurl(urlstr)
else:
	print '\n','抓取结果：\n','无匹配结果','\n'

