#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import pytesseract
from PIL import Image
import re
import webbrowser
from urllib import urlencode

sys.path.append("libs")
reload(sys)   
sys.setdefaultencoding('utf8')   


furl = 'https://www.baidu.com/s?wd='

def openurl(url):
	# url = 'https://www.baidu.com/s?wd=7%E2%80%B2%E6%B8%85%E6%9C%9D%E9%A1%BA%E6%B4%BD%E5%91%88%E5%B8%9D%E7%9A%84%E7%94%9F%E6%AF%8D%E6%98%AF%3F'

	# webbrowser.encode('gbk').open_new(url)
	webbrowser.open(url)
	# print webbrowser.get()


def getstr(imagepath):
	
	image = Image.open(imagepath)
	code = pytesseract.image_to_string(image,lang='chi_sim')
	print code



	# print arr
	# res = re.search(r'^[0-9]+\..*\n', code)

	# 将正则表达式编译成Pattern对象
	# pattern = re.compile(r'^[0-9]+\..*')
	res = re.search(r'[0-9]+.*\?', code,re.DOTALL)

	# if (res != None )& (len(res)==1 ):	
	# 	print '\n\n','抓取结果1：\n',res[0]
	if res :
		# print '\n','抓取结果：\n',res.group(),'\n'

		s = code.replace(res.group(), '')
		# 字符串分割成数组
		arr = s.split('\n')
		# 过滤空字符
		arr2 = [elem for elem in arr if elem != '']
		for x in range(len(arr2)):
			print x,':',arr2[x]

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



ans = getstr('testt/16.jpg')
if ans :
	print '\n','抓取结果：\n',ans,'\n'

	urlp = urlencode({'wd':ans})
	# print 
	# urlstr = furl+urlencode(ans)

	urlstr = 'https://www.baidu.com/s?%s'% urlp
	# print 'url:',urlstr


	openurl(urlstr)
	# openurl(urlstr)
else:
	print '\n','抓取结果：\n','无匹配结果','\n'

