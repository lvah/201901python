"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import random

import requests
from urllib.error import HTTPError
# 如何去模拟浏览器访问?


def get_content(url):
    try:
        user_agents = [
            "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
            "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        ]
        response = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
        response.raise_for_status()  # 如果状态码不是200， 引发HttpError异常
        # 从内容分析出响应内容的编码格式
        response.encoding = response.apparent_encoding
    except HTTPError as e:
        print(e)
    else:
        print(response.status_code)
        # print(response.headers)
        # return  response.text
        return response.content


if __name__ == '__main__':
    # url = 'https://www.amazon.cn/dp/B01ION3VWI'
    url = 'http://www.cbrc.gov.cn/chinese/jrjg/index.html'
    content = get_content(url)
    with open('doc/bank.html', 'wb') as f:
        f.write(content)

# 1. 京东商品页面信息的爬取;  https://item.jd.com/6789689.html
# 2. 亚马逊商品页面信息的爬取;https://www.amazon.cn/dp/B01ION3VWI


# BS4模块;  CSS样式===== id选择器， 类选择器， 属性选择器