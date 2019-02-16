"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import requests
from bs4 import BeautifulSoup
import re


def get_content(url,):
    try:
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
        response = requests.get(url,  headers={'User-Agent': user_agent})
        response.raise_for_status()   # 如果返回的状态码不是200， 则抛出异常;
        response.encoding = response.apparent_encoding  # 判断网页的编码格式， 便于respons.text知道如何解码;
    except Exception as e:
        print("爬取错误")
    else:

        print(response.url)
        print("爬取成功!")
        return  response.content


def parser_content(htmlContent):
    # 实例化soup对象， 便于处理；
    soup = BeautifulSoup(htmlContent, 'html.parser')
    # 1). 获取每个博客的大盒子： 特征: div标签, class名称一致article-item-box csdn-tracking-statistics
    #  <div class="article-item-box csdn-tracking-statistics" data-articleid="85718923">
    divObjs = soup.find_all('div', class_="article-item-box")
    # 2). 依次遍历每一个div标签， 获取博客标题
    #  博客标题的特征: h4里面的a标签里面的内容
    # 去掉默认的广告, 留下个人的博客内容;

    for  divObj in divObjs[1:]:
        # **2-1. 获取博客标题: 去掉原创或者转载的信息， 只需要博客名称;
        title = divObj.h4.a.get_text().split()[1]
        # **2-2. 获取博客链接， 也就是获取a链接中href对应的值；
        blogUrl = divObj.h4.a.get('href')
        global  bloginfo
        # 将爬取的所有内容保存到变量中[(blogtitle, blogurl)]
        bloginfo.append((title, blogUrl))


if __name__ == '__main__':
    blogPage = 3
    # 全局变量， 用于保存所有博客信息;
    bloginfo = []
    for page in range(1, blogPage+1):
        url = "https://blog.csdn.net/King15229085063/article/list/%s" %(page)
        content = get_content(url)
        parser_content(content)
        print("第%d页整理结束...." %(page))


    with open('doc/myblog.md', 'a') as f:
        for index, info in enumerate(bloginfo[::-1]):
            f.write('- 第%d篇博客: [%s](%s)\n' %(index+1, info[0], info[1]))
    print("完成.....")