# -*- coding: utf-8 -*-
from PIL import Image
import cv2

I = Image.open('testt/12.png')
I.show()
L = I.convert('L')   #转化为灰度图
L = I.convert('1')   #转化为二值化图
L.show()
