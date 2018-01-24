#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import pytesseract
from PIL import Image
import re
import webbrowser
from urllib import urlencode
import urllib2
from imghandle import handle 

sys.path.append("libs")
reload(sys)   
sys.setdefaultencoding('utf8')   


furl = 'https://www.baidu.com/s?wd='

def openurl(url):
	webbrowser.open(url)


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



# ans = getstr(handle('testt/13.jpg'))
# if ans :
# 	print '\n','抓取结果：\n',ans,'\n'

# 	urlp = urlencode({'wd':ans})
# 	# print 
# 	# urlstr = furl+urlencode(ans)

# 	urlstr = 'http://www.baidu.com/s?%s'% urlp

# 	page = urllib2.urlopen(urlstr).read()
# 	page = unicode(page, "utf-8")

# 	print 'urlstr:',urlstr
# 	# print '\n',page
# 	print '出现了', page.count("孝"),'次'
# 	# openurl(urlstr)
# 	# openurl(urlstr)
# else:
# 	print '\n','抓取结果：\n','无匹配结果','\n'

