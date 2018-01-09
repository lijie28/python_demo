import urllib.request
import os
import time


img_url_fo = 'http://wallpapers-girls.com/img/wallpapers/2.jpg'
# name = img_url.split('/')[-1]
# folder = img_url.split('/')[-2]
simple_url = 'http://wallpapers-girls.com/img/wallpapers/'


# url = simple_url + str(count) + '.jpg'

def download_img(count):
    the_url = simple_url + str(count) + '.jpg'
    img_name = str(count) + '.jpg'
    response = urllib.request.urlopen(the_url)

    if response.getcode() == 200:
        
        img = response.read()

        with open(img_name,'wb') as f:
            f.write(img)
        nextCount = count + 1 
        print ('下载 ',count)
        download_img(nextCount)
    else:
        print ('没有了')

# download_img(123)
print ('1')
time.sleep(5)#sleep 5s
print ('6')
# response = urllib.request.urlopen(img_url)
# isExists = os.path.exists(folder)
 
# if isExists:
#     print ('cz')
# else:
#     os.mkdir(folder)