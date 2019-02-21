# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response

from mySpider.items import csdnItem
from mySpider.settings import CsdnPage


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = [
        'https://blog.csdn.net/gf_lvah',
        # 'https://blog.csdn.net/gf_lvah',
    ]

    def parse(self, response):
        # 类似于字典的对象

        boxs = response.xpath('//div[@class="article-item-box csdn-tracking-statistics"]')

        for box in boxs:
            # 打印仅为了测试;
            # ************将item对象实例化在for循环里面， 否则每次会覆盖之前item的信息;*******
            item = csdnItem()
            item['title'] = box.xpath('./h4/a/text()')[1].extract().strip()
            item['url'] = box.xpath('./h4/a/@href')[0].extract()
            # print("1. *****************", item['title'])
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.parse_article)


        for page in range(2, 3):
            url = "https://blog.csdn.net/gf_lvah/article/list/%s" %(page)
            yield  scrapy.Request(url, callback=self.parse)

    def parse_article(self, response):
        item = response.request.meta['item']
        # 打印仅仅为了测试:出现问题的部分.
        # print("2.************************", item['title'])
        # inspect_response(response, self)
        content = response.xpath('//div[@id="article_content"]').extract()[0]
        item['content'] = 'aaa'
        yield item
