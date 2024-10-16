import scrapy


class ArtplastSpider(scrapy.Spider):
    name = "artplast"
    allowed_domains = ["artplast.ru"]
    start_urls = ["https://artplast.ru"]

    def parse(self, response):
        pass
