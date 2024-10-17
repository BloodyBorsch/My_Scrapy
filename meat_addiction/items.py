# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_name(value: list):
    result = value[1].capitalize()
    return result

def process_photo(value):
    url = "https://www.artplast.ru"
    value = url + value

class MeatAddictionItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor = TakeFirst())
    image = scrapy.Field(input_processor=MapCompose(process_photo))
    url = scrapy.Field(output_processor = TakeFirst())
    _id = scrapy.Field()

