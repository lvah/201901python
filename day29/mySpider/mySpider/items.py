# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # Item对象是一个简单容器， 保存爬取到的数据, 类似于字典的操作;
    # 实例化对象: course =  CourseItem()
    # course['title'] = "语文"
    # course['title']
    # course.keys()
    # course.values()
    # course.items()
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 课程链接， 课程的图片url， 课程的名称， 学习人数， 课程描述
    # 课程标题
    title = scrapy.Field()
    # 课程的url地址
    url = scrapy.Field()
    # 课程图片url地址
    image_url = scrapy.Field()
    # 课程的描述
    introduction = scrapy.Field()
    # 学习人数
    student = scrapy.Field()
