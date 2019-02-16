"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import requests
from bs4 import BeautifulSoup

def get_content(url):
    try:
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
        response = requests.get(url,  headers={'User-Agent': user_agent})
        response.raise_for_status()   # 如果返回的状态码不是200， 则抛出异常;
        response.encoding = response.apparent_encoding  # 判断网页的编码格式， 便于respons.text知道如何解码;
    except Exception as e:
        print("%s爬取错误" %(url))
    else:
        print(response.url)
        print("%s爬取成功!" %(url))
        return  response.content


def crawl_ips(page):
    headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    for i in range(1, page+1):
        response = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
        # 实例化soup对象， 便于处理；
        soup = BeautifulSoup(response.content, 'html.parser')