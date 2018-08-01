# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from meituan.items import MeituanItem
import pymongo


class MeituanPipeline(object):
    def __init__(self, MONGODB_HOST, MONGODB_PORT, MONGODB_DB):
        self.client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
        self.db = self.client[MONGODB_DB]

    @classmethod
    def from_settings(cls, settings):
        MONGODB_HOST = settings['MONGODB_HOST']
        MONGODB_PORT = settings['MONGODB_PORT']
        MONGODB_DB = settings['MONGODB_DB']

        return cls(MONGODB_HOST, MONGODB_PORT, MONGODB_DB)

    def process_item(self, item, spider):
        print('进入管道文件')
        if isinstance(item, MeituanItem):
            self.db['hotel'].insert(dict(item))
        
        return item

    def close_spider(self, spider):
        print('关闭爬虫')
        self.mongoCli.close()
