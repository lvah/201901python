# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item



class CsvPipeline(object):
    """将爬取的信息保存为csv格式"""

    def __init__(self):
        self.f = open('csdn.csv', 'w')

    def process_item(self, item, spider):
        # xxxx:xxxxx:xxxx
        item = dict(item)
        self.f.write("{0}:{1}:{2}\n".format(item['title'],  item['url'], item['content']))
        # 一定要加， 返回给调度为器；
        return item

    def open_spider(self, spider):
        """开启爬虫时执行的函数"""
        pass

    def close_spider(self, spider):
        """当爬虫全部爬取结束的时候执行的函数"""
        self.f.close()

