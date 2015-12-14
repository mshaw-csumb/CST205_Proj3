import scrapy
from tutorial.items import ShowItem

class CWSpider(scrapy.Spider):
    name = "cw"


    allowed_domains = ["cwtv.com"]
    start_urls = [
        "http://www.cwtv.com/shows/"
    ]

    def parse(self,response):
        #filename = response.url.split("/")[-2] + ".html"
        #with open(filename, 'wb') as f:
        #   f.write(response.body)

        for sel in response.xpath('//p'):
            item = ShowItem()
           # item['showTitle'] = sel.xpath('a/a/text()').extract()
            item['showTitle'] = sel.xpath('text()').extract()

            yield item
