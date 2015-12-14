import scrapy
from tutorial.items import ShowItem

class HuluSpider(scrapy.Spider):
    name = "hulu"


    allowed_domains = ["hulu.com"]
    start_urls = [
        "http://www.hulu.com/browse/tv",
        "http://www.hulu.com/movies/all"
    ]

    def parse(self,response):
        #filename = response.url.split("/")[-2] + ".html"
        #with open(filename, 'wb') as f:
        #   f.write(response.body)

        for sel in response.xpath('//a'):
            item = ShowItem()
           # item['showTitle'] = sel.xpath('a/a/text()').extract()
            item['showTitle'] = sel.xpath('text()').extract()

            yield item
