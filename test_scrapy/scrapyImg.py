import urllib.request
import os


img_url = 'http://img95.699pic.com/photo/50018/3487.jpg_wh300.jpg'

name = img_url.split('/')[-1]
folder = img_url.split('/')[-2]


response = urllib.request.urlopen(img_url)
isExists = os.path.exists(folder)
	
if isExists:
	print ('cz')
else:
	mkdir(folder)



# if response.getcode() == 200:
# 	img_path = response.read()
# 	with open(name,'wb') as f:
# 		f.write(img_path)



	