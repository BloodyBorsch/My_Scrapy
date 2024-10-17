# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pprint import pprint
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class MeatAddictionPipeline:
    def __init__(self):
        client = MongoClient("localhost", 27017)
        self.mongo_base = client.goods_16_10_2024

    def process_item(self, item, spider):
        #item["name"] = item.get("name")[1]
        item["name"] = item.get("name")
        collection = self.mongo_base[spider.name]
        collection.insert_one(item) 
        pprint(item)
        return item
    
class GoodsImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item["images"]:
            for img_url in item["images"]:
                try:
                    yield scrapy.Request(img_url)
                except Exception as e:
                    print(e)
        
    def item_completed(self, results, item, info):
        if results:
            item["images"] = [itm[0] for itm in results if itm[0] == True]
        return item
