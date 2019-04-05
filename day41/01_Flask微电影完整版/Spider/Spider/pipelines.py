# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class CsvPipeline(object):
    """将爬取的信息保存为csv格式"""

    def __init__(self):
        self.f = open('movie.csv', 'w')

    def process_item(self, item, spider):
        # xxxx:xxxxx:xxxx
        item = dict(item)
        import csv
        writer = csv.writer(self.f)
        writer.writerow(item.values())
        # 一定要加， 返回给调度为器；
        return item

    def open_spider(self, spider):
        """开启爬虫时执行的函数"""
        pass

    def close_spider(self, spider):
        """当爬虫全部爬取结束的时候执行的函数"""
        self.f.close()


import scrapy


# scrapy框架里面，
# #自定义一个类,继承于ImagesPipeline,对ImagesPipeline进行重写,以实现自己需要的功能
class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # print(item['logo'])
        # 返回一个request请求， 包含图片的url地址
        yield scrapy.Request(item['logo'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        name = item['name']
        img_name = item['name'] + item['logo'].split('/')[-1]
        return img_name

    # 当下载请求完成后执行的函数/方法
    def item_completed(self, results, item, info):
        # 提取用户的源文件名
        # open('mooc.log', 'w').write(results)
        # print(results)
        #  获取下载的地址ls
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise Exception("不包含图片")
        else:
            return item
