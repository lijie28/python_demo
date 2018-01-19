#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from skimage import io
import matplotlib.pyplot as plt
# from __future__ import print_function
image=io.imread('testt/16.jpg')

# 看看图片的类型，上诉io.imread读取的过程，实际上将image转化成数组的形式
print(type(image)) #<class 'numpy.ndarray'>
# 此时，可以打印出图片看一看,打开的图片也就是第一张大家看到的原图
plt.imshow(image)