# -*- coding: utf-8 -*-
import scrapy
from Spider.items import MovieItem
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = [
        'https://maoyan.com/board',
        'https://maoyan.com/board/2',
        'https://maoyan.com/board/4',
        'http://maoyan.com/board/1',
        'https://maoyan.com/board/6',

    ]
    prefix_url = 'https://maoyan.com'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        movies = response.xpath('//dl[@class="board-wrapper"]/dd')
        for movie in movies:
            movieItem = MovieItem()
            movieItem['name'] = movie.xpath('./a/@title')[0].extract()
            movieItem['logo'] = movie.xpath('./a/img[@class="board-img"]/@data-src')[0].extract().split('@')[0]
            movie_info = movie.xpath('./div[@class="board-item-main"]/div[@class="board-item-content"]/'
                                     'div[@class="movie-item-info"]')
            movieItem['actors'] = movie_info.xpath('./p[@class="star"]/text()')[0].extract().strip().strip("主演：")
            movieItem['release_time'] = movie_info.xpath('./p[@class="releasetime"]/text()')[0].extract().strip("上映时间：")

            movieItem['detailUrl'] = self.prefix_url + movie.xpath('./a/@href')[0].extract()

            yield scrapy.Request(movieItem['detailUrl'], callback=self.parse_detail_movie,
                                 meta={'movieItem': movieItem})
            # yield movieItem

        # url跟进, 获取下一页是否有链接;href
        url = response.xpath('//a[contains(text(), "下一页")]/@href').extract()
        if url:
            # 构建新的url
            page = response.url.split('?')[0] + url[0]
            yield scrapy.Request(page, callback=self.parse)

    def parse_detail_movie(self, response):
        movieItem = response.request.meta['movieItem']
        # ['<li class="ellipsis">动画,动作,冒险</li>', '<li class="ellipsis">\n        美国\n          / 104分钟\n        </li>', '<li class="ellipsis">2019-03i>']
        ellipsis = response.xpath('//ul/li[@class="ellipsis"]')

        # ['动作,冒险,科幻']  === 只获取第一个标签即可
        movieItem['tag'] = ellipsis[0].xpath('./text()').extract()[0].split(',')[0]
        #  \n        美国\n          / 104分钟\n       === 美国 104分钟
        all_area_length = ellipsis[1].xpath('./text()')[0].extract().strip().split('/')
        movieItem['area'], movieItem['length'] = all_area_length[0].strip(), all_area_length[1].strip()
        movieItem['info'] = response.xpath('//span[@class="dra"]/text()')[0].extract()
        print(dict(movieItem))
        return movieItem
