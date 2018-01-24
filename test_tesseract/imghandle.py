#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from skimage import data, exposure, img_as_float, io, img_as_ubyte
import matplotlib.pyplot as plt


# 

def hv(img_data,k):
	#调整曝光度 handel_visibility
	gam= exposure.adjust_gamma(img_data, k)   
	return gam

def hc(img_data,k):
	#对比度 handle_contrast
	gam= exposure.adjust_log(img_data,k)   #对数调整
	return gam

def hs(img_data,k):
	#对比度 handle_contrast
	gam= exposure.adjust_sigmoid(img_data,k)   #对数调整
	return gam



def hr(img_data):
	#更改对比度范围，让颜色变得更加鲜亮
 	gam= exposure.rescale_intensity(img_data,in_range=(0.25,0.55))
 	# gam= exposure.rescale_intensity(img_data,0.4)
 	return gam

def plt_show(img_data):
	plt.figure('adjust_gamma',figsize=(8,8))
	plt.subplot(131)
	plt.title('gamma')
	plt.imshow(img_data,plt.cm.gray)
	plt.axis('off')
	plt.show()


def save_imgdata(img_data,img_path):
	io.imsave(img_path,img_data)

	# img_data.save('test.jpg')
# imgdata = hc(hs(hv(image,4),0.3),1.1)

# imgdata = hr(image)

def handle(img_path):
	image=io.imread(img_path,as_grey=False)
	image = img_as_float(image)
	imgdata = hs(hv(image,9),0.1)
	# save_imgdata(img_path,imgdata)
	io.imsave(img_path,imgdata)
	print 'over'
	return img_path



# img_path='testt/13.jpg'
# img = handle(img_path)
# save_imgdata(img,'testt/hah.jpg')
# plt_show(imgdata)
# save_imgdata(imgdata)



# from skimage import data, exposure, img_as_float, io
# import matplotlib.pyplot as plt

# img_name='testt/13.jpg'
# img=io.imread(img_name,as_grey=False)
# image = img_as_float(img)



