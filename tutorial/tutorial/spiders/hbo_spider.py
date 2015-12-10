import scrapy
from tutorial.items import ShowItem


class HboSpider(scrapy.Spider):
    name = "hbo"


    allowed_domains = ["hbo.com"]
    start_urls = [
        "http://www.hbo.com/schedule/hbonow-hbogo?category=Series"
    ]

    def parse(self,response):
        filename = response.url.split("/")[-2] + ".html"
        with open(filename, 'wb') as f:
            f.write(response.body)

        for sel in response.xpath('//span'):
            item = ShowItem()
           # item['showTitle'] = sel.xpath('a/a/text()').extract()
            item['showTitle'] = sel.xpath('text()').extract()

            yield item
