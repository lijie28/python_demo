# -*- coding: utf-8 -*-

# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

import pytesseract
from PIL import Image
import re
the_str = "1.This 3.2 is some text -- with punctuation" 
    # This

image = Image.open('testt/12.png')
code = pytesseract.image_to_string(image,lang='chi_sim')

print code

for x in code.split('?'):
	print '分割：',x

# res = re.search(r'^[0-9]+\..*\n', code)

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'^[0-9]+\..*\n')
res = re.search(pattern, code)

if res :	
	print '\n\n','抓取结果：\n',res.group() 
else:
	print '\n\n','抓取结果：\n','无匹配结果'