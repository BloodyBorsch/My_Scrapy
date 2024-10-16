import scrapy
from scrapy.http import HtmlResponse


class ArtplastSpider(scrapy.Spider):
    name = "artplast"
    allowed_domains = ["artplast.ru"]
    start_urls = ["https://www.artplast.ru/catalog/bumazhnye-pakety/"]

    def parse(self, response: HtmlResponse):
        links = response.xpath('//div[contains(@x-data, "price_block")]//a/@href').getall()

        for link in links:
            yield response.follow(link, callback=self.items_parse)

        print(response.status, response.url)

    def items_parse(self, response: HtmlResponse):
        print()
