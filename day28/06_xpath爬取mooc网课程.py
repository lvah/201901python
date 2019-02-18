"""
文件名: $NAME.py
日期: 18  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



- 爬取的链接: http://www.imooc.com/course/list
- 爬取的内容: 课程链接， 课程的图片url， 课程的名称， 学习人数， 课程描述
- 爬取的内容如何存储:
    - 文件(.csv, );
    - mysql数据库;
- 分析爬取的信息;
    - 词云

"""
import re

import requests
import lxml.etree as etree
import csv


def get_content(url):
    """爬取页面内容的函数"""

    try:
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
        response = requests.get(url, headers={'User-Agent': user_agent})
        response.raise_for_status()  # 如果返回的状态码不是200， 则抛出异常;
        response.encoding = response.apparent_encoding  # 判断网页的编码格式， 便于respons.text知道如何解码;
    except Exception as e:
        print("爬取错误")
    else:

        print(response.url)
        print("爬取成功!")
        return response.content


def parser_content(html):
    """分析页面获取需要的信息:课程链接， 课程的图片url， 课程的名称， 学习人数， 课程描述 """
    # 1). 将html内容转化成xpath可以解析/匹配的格式;
    selector = etree.HTML(html)

    # 2). 获取每个课程的信息: <div class="course-card-container">
    courseDetails = selector.xpath('//div[@class="course-card-container"]')

    courseInfos = []
    for courseDetail in courseDetails:
        # 课程的名称： <h3 class="course-card-name">初识HTML+CSS</h3>
        name = courseDetail.xpath('.//h3[@class="course-card-name"]/text()')[0]

        # 学习人数
        """
        <div class="course-card-info">
					<span>入门</span><span><i class="icon-set_sns"></i>1000167</span>
				</div>
        """
        studentNum = courseDetail.xpath('.//span/text()')[1]

        # 课程描述: <p class="course-card-desc">HTML+CSS基础教程8小时带领大家步步深入学习标签用法和意义</p>
        courseInfo = courseDetail.xpath(".//p[@class='course-card-desc']/text()")[0]
        # print(name, studentNum, courseInfo)

        # 课程链接， h获取/learn/9 ====》 http://www.imooc.com/learn/9
        # <a target="_blank" href="/learn/9" class="course-card">
        courseUrl = "http://www.imooc.com" + courseDetail.xpath('.//a/@href')[0]
        # print(courseUrl)

        # 课程的图片url:
        """
        <img class="course-banner lazy" data-original="//img1.mukewang.com/529dc3380001379906000338-240-135.jpg" 
        src="//img1.mukewang.com/529dc3380001379906000338-240-135.jpg" style="display: inline;">
        """
        courseImgUrl = 'http:' + courseDetail.xpath('.//img/@src')[0]

        courseInfos.append((name, studentNum, courseInfo, courseUrl, courseImgUrl))

    return courseInfos


def save_csv(courseInfo):
    """将获取的课程信息保存为csv格式"""

    with open('doc/mooc.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(courseInfo)
    print("csv文件保存成功........")


def save_json(courseInfo):
    """将获取的信息保存为json格式"""
    import json
    with open('doc/mooc.json', 'w', encoding='utf-8') as f:
        for item in courseInfo:
            item = {
                'name': item[0],
                'studentNum': item[1],
                'courseInfo': item[2],
                'courseUrl': item[3],
                'courseImgUrl': item[4]
            }
            # ensure_ascii： 如果有中文， 则设置为False， 表示使用Unicode编码， 中文不会乱码;
            #  indent=4: 所金为4个空格， 便于阅读;
            jsonitem = json.dumps(item, ensure_ascii=False, indent=4)
            f.write(jsonitem + '\n')
    print("json文件保存成功......")





def moocSpider():
    # 1). 爬取课程信息的第一页
    url = "http://www.imooc.com/course/list"
    html = get_content(url=url)
    courseInfos = parser_content(html)  # 列表， 保存第一也的课程信息;
    # 2). 如果有下一页信息， 则继续爬取课程内容;
    #     如果没有下一页信息， 则跳出循环， 将课程信息保存到文件中.....;
    #
    while True:
        # 获取是否拥有下一页?
        selector = etree.HTML(html)
        nextPage = selector.xpath('//a[contains(text(), "下一页")]/@href')
        print(nextPage)
        # 只爬取前2页， 用于测试;
        # if nextPage and ('3' not in nextPage[0]):
        if nextPage:
            url = "http://www.imooc.com" + nextPage[0]
            html = get_content(url=url)
            otherCourseInfo = parser_content(html)
            courseInfos += otherCourseInfo  # 把其他页获取的页面信息追加到变量中;
        else:
            print("全部爬取结束......")
            break

    # print(courseInfos)
    save_csv(courseInfos)
    save_json(courseInfos)

    # #  1). 课程信息有多页， url规则：
    # """
    # 两种url均可:
    # http://www.imooc.com/course/list?page=28
    # http://www.imooc.com/course/list?page=1
    #
    # http://www.imooc.com/course/list/2
    # http://www.imooc.com/course/list/28
    # """
    #
    # # 2).  什么时候爬取结束? 没有下一页的时候
    # """
    # # 有下一页:
    #     <a href="/course/list/2?page=2">下一页</a>
    #
    # # 没有下一页:
    #     <span class="disabled_page">下一页</span>
    #
    # """
    #
    #


def dealCourseData(filename):
    """对于爬取的课程信息进行分析， 返回清洗好的数据"""
    #
    wordcloudString = ''
    # 读取需要的文件内容
    with open(filename) as f:
        reader = csv.reader(f)
        # 清洗需要分析的文本信息: 删除里面不必要的逗号， 句号， 表情;
        pattern = re.compile(r'([\u4e00-\u9fa5]+|[a-zA-Z0-9]+)')
        for item in reader:
            # 将来进行词云展示时， 需要的是字符串， 而不是列表;
            name = "".join(re.findall(pattern, item[0]))
            detail = "".join(re.findall(pattern, item[2]))
            wordcloudString += name
            wordcloudString += detail

        return  re.sub(r'(学习|使用|入门|基础|实现|掌握)', '', wordcloudString)


import re
import jieba
from PIL import Image
from wordcloud import wordcloud
import numpy as np


def gen_wordcloud(text, filename):
    # 1). 强调分割中有问题的词;
    # jieba.suggest_freq(('微博'), True)
    # jieba.suggest_freq(('热搜'), True)

    #  2). 难点: 如何切割中文, jieba, lcut
    result = jieba.lcut(text)
    # print(result)

    # 绘制词云
    # 3). 打开图片， 获取图片的数据信息;
    imgObj = Image.open('./doc/wordcloud.jpg')
    img_mask = np.array(imgObj)
    # print(img_mask)
    # 4). 创建词云对象， 设置属性
    wcObj = wordcloud.WordCloud(
        mask=img_mask,  # 数据如何填充到图片
        background_color="snow",  # 北京颜色
        font_path="/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc",  # 如果是中文， 指定字体库(fc-list :lang=zh)
        min_font_size=5,  # 图片中最小的字体大小
        max_font_size=50,  # 图片中最小的字体大小
        width=1000,  # 图片宽度
        height=1000,  # 高
    )
    # 5). 生成图片;
    # 词云绘制时， 默认之处理字符串类型， 怎么分隔每个单词? 必须以逗号分隔符分割
    wcObj.generate(",".join(result))
    wcObj.to_file(filename)
    print("生成图片%s成功......." %(filename))


if __name__ == '__main__':
    # 爬取数据信息
    # moocSpider()

    # 分析爬取的数据
    text = dealCourseData('doc/mooc.csv')
    filename = "doc/mooc.png"
    gen_wordcloud(text, filename)

