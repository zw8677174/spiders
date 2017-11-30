import scrapy
from ..models.db import Bilibili


class QuotesSpider(scrapy.Spider):
    name = "bilibili"
    urls = []

    def start_requests(self):
        for i in range(1, 2000000):
            self.urls.append('https://www.bilibili.com/video/av' + str(i))
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name = response.xpath('//h1/text()').extract_first()
        if name is not None:
            print(name)
            Bilibili.insert(name=name).execute()
