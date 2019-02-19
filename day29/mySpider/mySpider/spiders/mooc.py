# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import CourseItem



class MoocSpider(scrapy.Spider):
    # name: 用于区别爬虫, 必须是唯一的；
    name = 'mooc'
    # 允许爬取的域名；其他网站的页面直接跳过;
    allowed_domains = ['www.imooc.com', 'img3.mukewang.com']
    # 爬虫开启时第一个放入调度器的url地址;
    start_urls = ['http://www.imooc.com/course/list']

    # 被调用时， 每个出世url完成下载后， 返回一个响应对象,
    # 负责将响应的数据分析， 提取需要的数据items以及生成下一步需要处理的url地址请求;
    def parse(self, response):

        # # 用来检测代码是否达到指定位置， 并用来调试并解析页面信息;
        # from scrapy.shell import  inspect_response
        # inspect_response(response, self)

        # 1). 实例化对象， CourseItem
        course = CourseItem()
        # 分析响应的内容
        # scrapy分析页面使用的是xpath语法
        # 2). 获取每个课程的信息: <div class="course-card-container">
        courseDetails = response.xpath('//div[@class="course-card-container"]')
        for courseDetail in courseDetails:
            # 课程的名称：
            # "htmlxxxx"


            # 爬取新的网站， Scrapy里面进行调试(parse命令logging)
            course['title'] = courseDetail.xpath('.//h3[@class="course-card-name"]/text()').extract()[0]
            # 学习人数
            course['student'] = courseDetail.xpath('.//span/text()').extract()[1]
            # 课程描述:
            course['introduction'] = courseDetail.xpath(".//p[@class='course-card-desc']/text()").extract()[0]
            # 课程链接， h获取/learn/9 ====》 http://www.imooc.com/learn/9
            course['url'] = "http://www.imooc.com" + courseDetail.xpath('.//a/@href').extract()[0]
            # 课程的图片url:
            course['image_url'] = 'http:' + courseDetail.xpath('.//img/@src').extract()[0]

            yield  course



            # url跟进, 获取下一页是否有链接;href
            url  = response.xpath('.//a[contains(text(), "下一页")]/@href')[0].extract()
            if url:
                # 构建新的url
                page = "http://www.imooc.com" + url
                yield scrapy.Request(page, callback=self.parse)


