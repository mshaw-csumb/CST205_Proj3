import scrapy
from tutorial.items import FoxShowItem


class FoxSpider(scrapy.Spider):
    name="fox"

    allowed_domains = ["fox.com"]
    start_urls = [
        "http://www.fox.com/shows"
    ]

    def parse(self,response):
        filename = response.url.split("/")[-2] + ".html"
        with open(filename, 'wb') as f:
            f.write(response.body)

        #for sel in response.xpath('//div[@class="views-field views-field-title"]/span[@class="field-content"]/a'):
        for sel in response.xpath('//div[@class="field-content show-id"]'):
            item = FoxShowItem()
           # item['showTitle'] = sel.xpath('a/a/text()').extract()
            item['showTitle'] = sel.xpath('text()').extract()

            yield item
