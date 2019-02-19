"""
文件名: $NAME.py
日期: 19  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




# 爬取的步骤
    - 确定url地址;
    - 获取页面信息;(urllib, requests);
    - 解析页面提取需要的数据； (正则表达式， bs4， xpath)
    - 保存到本地(csv, json, pymysql, redis);
    - 清洗数据(删除不必要的内容 -----正则表达式);
    - 分析数据(词云wordcloud + jieba)

有没有用到多线程?    -----
获取页面信息每个爬虫都会使用， 重复去写----
设置头部信息 ---- user-agent, proxy....





# 流程分析:
    - 确定url地址:http://www.imooc.com/course/list;(spider)
    - 获取页面信息;(urllib, requests); ---(scrapy中我们不要处理)---(Downloader)
    - 解析页面提取需要的数据； (正则表达式， bs4， xpath)---: (spider)
        课程链接， 课程的图片url， 课程的名称， 学习人数， 课程描述
    - 保存到本地(csv, json, pymysql, redis); ----(pipeline)



# 环境
    - Scrapy 1.6.0




# 实现步骤：
1. 工程创建
 scrapy  startproject mySpider
 cd mySpider
 tree
├── mySpider
│   ├── __init__.py
│   ├── items.py            # 提取的数据信息
│   ├── middlewares.py      # 中间键
│   ├── pipelines.py        # 管道， 如何存储数据
│   ├── __pycache__
│   ├── settings.py         # 设置信息
│   └── spiders             # 爬虫(解析页面的信息)
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg



2. 创建一个爬虫
scrapy  genspider  mooc "www.imooc.com"
cd mySpider/spiders/
vim mooc.py
# start_url



3. 定义爬取的items内容
class CourseItem(scrapy.Item):
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



# 4. 编写spider代码, 解析


"""