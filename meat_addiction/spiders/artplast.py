import scrapy
from scrapy.http import HtmlResponse
from items import MeatAddictionItem


class ArtplastSpider(scrapy.Spider):
    name = "artplast"
    allowed_domains = ["artplast.ru"]
    start_urls = ["https://www.artplast.ru/catalog/korobki-dly-piccy/"]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[@class="relative flex items-center space-x-3 duration-200 group text-gray hover:text-body"]').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//div[contains(@x-data, "price_block")]//div[@class="relative"]/a/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.items_parse)    

    def items_parse(self, response: HtmlResponse):
        name = response.xpath('.//ul[contains(@class, "space-y-3")]/li[contains(@class, "relative flex items-end")]/span/text()').getall()
        image = response.xpath('//img[contains(@itemprop, "image")]/@src').getall()
        url = response.url
        yield MeatAddictionItem(name=name, image=image, url=url)