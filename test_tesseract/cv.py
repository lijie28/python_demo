# -*- coding: utf-8 -*-
#导入cv模块
# import cv2 as cv
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
import cv2
import numpy as np
from matplotlib import pyplot as plt


def creatWindow():
	img = cv.imread('testt/13.jpg')
	#创建窗口并显示图像
	cv.namedWindow("Image")
	cv.imshow("Image",img)
	cv.waitKey(0)
	#释放窗口
	cv2.destroyAllWindows()


def arangeGray():
	img=cv2.imread('testt/13.jpg')
	# gray = cv2.imread('testt/12.png',0)
	GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
	ret,thresh2=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)
	ret,thresh3=cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)
	ret,thresh4=cv2.threshold(GrayImage,1,255,cv2.THRESH_TOZERO)
	ret,thresh5=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)
	titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
	images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
	for i in xrange(6):
	   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	   plt.title(titles[i])
	   plt.xticks([]),plt.yticks([])
	plt.show()

arangeGray()