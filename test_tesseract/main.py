#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import os
from jt import screenshot 
from tt import getstr as reconize
from imghandel import handle 

folder = 'result2'
imgtype = '.jpeg'


if os.path.exists(folder) == False:
	os.makedirs(folder)

time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
path = folder + '/' +time + imgtype

print path



def funcA(kws):
	print kws,'a'

def funcB(kws,func):
	s = kws + 'b'
	print s
	func(s)

funcB ('ans:',funcA)

# screenshot(path,reconize)
# handle(path)
# reconize(path)