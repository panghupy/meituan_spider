# -*- coding: utf-8 -*-(
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
import json
import re
from meituan.items import MeituanItem
import requests
import os


class MeituanSpiderSpider(Spider):
    name = 'meituan_spider'
    allowed_domains = ['meituan.com']
    start_urls = [
        'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=4C4844EA1E383289F62BCF8C630947BC4DA3121E283B39A9EF152D2C34203C23%401533035734323&cityId=96&offset=0&limit=20&startDay=20180731&endDay=20180731&q=&sort=defaults&X-FOR-WITH=14%2FqUl622CaRIB0XobpocXLZRvKEUIWbrzBk%2BTGfRG79yI5uZ60MWS%2BwGukD4LfoDQ%2BVr%2BQFEJQOTlTggX031A4wTNWNW1rEcwxOSyFjHbQK6x1dLtpcn9xIOIfd%2F%2BdCWXRVaKJX7Sc9TSdBPzjiJg%3D%3D']
    offset = 0

    # 拿到酒店数据和id
    def parse(self, response):
        self.offset += 20
        result = json.loads(response.text)
        # 拿到酒店信息和id，id用来构造请求照片的链接
        for i in result['data']['searchresult']:
            item = MeituanItem()
            item['name'] = i['name']
            item['poiid'] = i['poiid']
            # 价格-多少元起
            item['originalPrice'] = i['originalPrice']
            # 地址
            item['addr'] = i['addr']
            # 评论数
            item['commentsCountDesc'] = re.search('\d+', i['commentsCountDesc']).group()
            # 评分
            item['avgScore'] = i['avgScore']
            # 所属商圈
            item['areaName'] = i['areaName']
            # 标签
            item['poiAttrTagList'] = i['poiAttrTagList']
            meta = {
                'name': i['name']
            }
            yield item
            # 请求酒店图片的接口
            get_img_url = 'https://ihotel.meituan.com/group/v1/poi/' + str(
                i[
                    'poiid']) + '/imgs?utm_medium=touch&version_name=999.9&classified=true&X-FOR-WITH=s99Eh6sbSKFk2CtgH69UM3vUAY6t0ETpasHKECThU0OOv6duCovPaszE2v8xYNb0y5tFbd0R1Bz7HxqoWbDCnlQzCaz1U%2FWG2Is1UD6ycN%2Fv5sM9vSw%2BtMe6IAQAogdarTlC3CQPD6IfxiaVmV005g%3D%3D'
            yield scrapy.Request(get_img_url, callback=self.parse_img, meta=meta)
        next_page_url = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=4C4844EA1E383289F62BCF8C630947BC4DA3121E283B39A9EF152D2C34203C23%401533035734323&cityId=96&offset=' + str(
            self.offset) + '&limit=20&startDay=20180731&endDay=20180731&q=&sort=defaults&X-FOR-WITH=14%2FqUl622CaRIB0XobpocXLZRvKEUIWbrzBk%2BTGfRG79yI5uZ60MWS%2BwGukD4LfoDQ%2BVr%2BQFEJQOTlTggX031A4wTNWNW1rEcwxOSyFjHbQK6x1dLtpcn9xIOIfd%2F%2BdCWXRVaKJX7Sc9TSdBPzjiJg%3D%3D'
        yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_img(self, response):
        '''获取酒店的图片并保存到本地'''
        hotel_name = response.meta['name']
        result = result = json.loads(response.text)
        os.mkdir('./' + hotel_name)
        for i in result['data']:
            for j in i['imgs']:
                img_url = j['urls'][0]
                img_url = re.sub('w.h', '750.0', img_url)
                img_response = requests.get(img_url).content
                filename = './' + hotel_name + '/' + img_url[-10:]
                print('下载图片')
                with open(filename, 'wb')as f:
                    f.write(img_response)
