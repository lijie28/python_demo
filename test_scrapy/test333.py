# -*- coding: utf-8 -*-
from lxml import etree

filename = 'suning.html' 
def getFileHtml(filename):
    '''
    获取指定url返回页的所有文字
    :param url: 需要抓取的url
    :return: 返回文字
    '''
    page = open(filename,'r').read()
    # page = urllib2.urlopen(url, timeout=10).read()
    page = unicode(page, "utf-8")  # 转换编码,否则会导致输出乱码
    # cleaner = Cleaner(style=True, scripts=True, page_structure=False, safe_attrs_only=False)  # 清除掉CSS等
    selector = etree.HTML(page)
    # shops = selector.xpath('//div[@class="store-info"]/ul/li/span[@class="title"]')
    shops = selector.xpath('//div[@class="store-info"]')
    return shops


print getFileHtml(filename)
# for index in getFileHtml(filename):
#     print index.text