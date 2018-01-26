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



