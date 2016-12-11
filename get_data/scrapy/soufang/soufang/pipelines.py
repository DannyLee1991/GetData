# -*- coding: utf-8 -*-
import re
import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 剔除html代码
def take_out_html(str):
    dr = re.compile(r'<[^>]+>', re.S)
    return dr.sub('', str)


class ExtractDataPipeline(object):
    def process_item(self, item, spider):
        print ">>> ExtractDataPipeline >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        self.extract_data(item, "url")
        self.extract_data(item, "id", f=5)
        self.extract_data(item, "publish_time", f=-10)
        self.extract_data(item, "title")
        self.extract_data(item, "total_price")
        self.extract_data(item, "house_type", f=3)
        self.extract_data(item, "house_build_area", f=5)
        self.extract_data(item, "house_use_area", f=5)
        self.extract_data(item, "house_age", f=3)
        self.extract_data(item, "orientation", f=3)
        self.extract_data(item, "floor", f=3)
        self.extract_data(item, "structure", f=3)
        self.extract_data(item, "decoration", f=3)
        self.extract_data(item, "residential_category", f=5)
        self.extract_data(item, "building_class", f=5)
        self.extract_data(item, "property_right", f=5)
        self.extract_data(item, "property_name")
        self.extract_data(item, "school")
        self.extract_data(item, "supporting_facilities")
        self.extract_data(item, "bread_city", t=-3)
        self.extract_data(item, "bread_area", t=-3)
        self.extract_data(item, "bread_positon", t=-3)
        return item

    # 剔除数据中的多余部分
    def extract_data(self, item, key_bread_positon, f=None, t=None):
        if self.check_key_exist(item, key_bread_positon):
            item[key_bread_positon] = take_out_html(item[key_bread_positon]).strip()[f:t]
        else:
            item[key_bread_positon] = ""
        self.print_itme_value(item, key_bread_positon)

    # 检查key是否存在
    def check_key_exist(self, item, key):
        return key in item.keys()

    # 输出数据
    def print_itme_value(self, item, key):
        print key + " >>> " + item[key]

class SaveDataPipline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print ">>> SaveDataPipline >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        collection_name = self.mongo_db
        self.db[collection_name].insert(dict(item))
        return item
