import urllib.request
import os
import time


img_url_fo = 'http://wallpapers-girls.com/img/wallpapers/2.jpg'
# name = img_url.split('/')[-1]
# folder = img_url.split('/')[-2]
simple_url = 'http://wallpapers-girls.com/img/wallpapers/'


# url = simple_url + str(count) + '.jpg'

def image_download(func):
    def in_image_download(url):
        #先把url放response里测反应
        func(url)
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            name = url.split('/')[-1]
            folder = url.split('/')[-2]
            img = response.read()
            with open(name,'wb') as f:
                f.write(img)

            return in_image_download
        else:
            print ('没有了')

# download_img(123)
# print ('1')
# time.sleep(5)#sleep 5s
# print ('6')
# response = urllib.request.urlopen(img_url)
# isExists = os.path.exists(folder)
 
# if isExists:
#     print ('cz')
# else:
#     os.mkdir(folder)