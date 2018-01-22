#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from skimage import data, exposure, img_as_float, io, img_as_ubyte
import matplotlib.pyplot as plt


img_name='testt/13.jpg'
image=io.imread(img_name,as_grey=True)
image = img_as_float(image)
# image = img_as_float(data.moon())

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


def save_imgdata(img_data):
	io.imsave('testt/testsave.jpg',img_data)

	# img_data.save('test.jpg')
# imgdata = hc(hs(hv(image,4),0.3),1.1)

# imgdata = hr(image)

imgdata = hs(hv(image,9),0.1)

# plt_show(imgdata)
save_imgdata(imgdata)



# from skimage import data, exposure, img_as_float, io
# import matplotlib.pyplot as plt

# img_name='testt/13.jpg'
# img=io.imread(img_name,as_grey=False)
# image = img_as_float(img)





# from skimage import io,data,color
# import matplotlib.pyplot as plt
# from skimage.morphology import disk
# import skimage.filters.rank as sfr


# img_name='testt/13.jpg'
# img=io.imread(img_name,as_grey=False)
# img=color.rgb2gray(img)
# auto =sfr.enhance_contrast(img, disk(5))
# plt.figure('filters') 
# plt.subplot(121)
# plt.imshow(img,plt.cm.gray) 
# plt.subplot(122) 
# plt.imshow(auto,plt.cm.gray)
# plt.show()



# img_name='testt/15.jpg'
# img=io.imread(img_name,as_grey=False)
# img_gray=color.rgb2gray(img)
# io.imshow(img_gray)
# io.show()