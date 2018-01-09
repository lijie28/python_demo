import scrapy


class SeleniumSpider(scrapy.CrawlSpider):
    name = "SeleniumSpider"
    start_urls = ["https://www.facebook.com"]

    def parse(self, response):
        hxs = Selector(response)
        print hxs.xpath('//a[contains(@href, "html")]').extract()


class QuotesSpider(scrapy.Spider):
    name = "wb"

    def start_requests(self):
        urls = [
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
            'https://weibo.cn'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        filename = 'test-wb.html' 
        with open(filename, 'wb') as f:
            f.write(response.body)