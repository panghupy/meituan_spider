# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanItem(scrapy.Item):
    name = scrapy.Field()
    poiid = scrapy.Field()
    # 价格-多少元起
    originalPrice = scrapy.Field()
    # 地址
    addr = scrapy.Field()
    # 评论数
    commentsCountDesc = scrapy.Field()
    # 评分
    avgScore = scrapy.Field()
    # 所属商圈
    areaName = scrapy.Field()
    # 标签
    poiAttrTagList = scrapy.Field()