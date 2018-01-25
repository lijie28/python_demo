#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import os
from jt import screenshot 
from tt import getstr as reconize
from imghandle import handle 

folder = 'result2'
imgtype = '.jpeg'

if os.path.exists(folder) == False:
    os.makedirs(folder)

time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
path = folder + '/' +time + imgtype
print path



def deal(path):
    print 'deal begin'
    handle(path)
    reconize(path)
    print 'deal over'



screenshot(deal,path)

def test(outfunc,b,path):
	print 'her'
	print b ,path
	return outfunc(path)

def test2(path):
	print 'outfunc is to do :',path

# a = lambda x,y : x+y

# a = test(3)

def testAdaptor(func, outfunc, **kwds):
	print 'testAdaptor'
	# return func(outfunc,**kwds)
	return lambda fun, outfunc=outfunc : fun(outfunc,**kwds)




# a = testAdaptor(test,test2,b='path is :',path='test/')

# print a('1')


# def funcA( kws):
# 	print kws,'a'

# def funcB(kws,func):
# 	s = kws + 'b'
# 	print s
# 	return funcA(s)
# 	# func(s)

# funcB ('ans:',funcA)

# handle(path)
# reconize(path)