# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals


class UserAgentMiddleware(object):
    def __init__(self):
        self.user_agent = [
            'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        ]
    def process_request(self, request, spider):
        ua = random.choice(self.user_agent)
        if ua:
            # 此行仅为了测试, 真实场景不要打印， 会影响爬虫的效率
            # print("当前使用的用户代理: %s" %(ua))
            request.headers.setdefault('User-Agent', ua)





class ProxiesMiddleware(object):
    # 留下练习:
    #       - 1). 从西刺代理IP网站获取所有的代理IP并存储到mysql/redis;
    def __init__(self):
        # 2). 连接redis/mysql数据库；

        self.proxies = [
            'http://116.209.54.221:9999',
            "https://111.177.183.212:9999"
        ]
    def process_request(self, request, spider):
        """当发起请求"""
        # 3). 从数据库里面随即获取一个代理IP；
        proxy = random.choice(self.proxies)

        if proxy:
            # 此行仅为了测试, 真实场景不要打印， 会影响爬虫的效率
            # print("当前使用的代理IP： %s" %(proxy))
            request.meta['proxy'] = proxy

    # def process_response(self, response, spider):
    #     """当响应的时候自动执行的函数......"""
    #     pass
    # def process_exception(self, request, exception, spider):
    #     if exception:
    #         # 4). 如果产生异常， 则删除数据库里面对应的数据;
    #         print("代理异常")
    #     return  request



class MyspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
