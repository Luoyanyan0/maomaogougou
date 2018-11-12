# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class MaomaogougouPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for url in item['url']:
            yield Request(url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        img_title = item['img_title']+'.jpg'
        big_dir_name = item['big_dir_name']
        # time=strftime("%Y-%m-%d", gmtime())
        return 'maomaogougouImg/%s/%s' % (big_dir_name,img_title)



