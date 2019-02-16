"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


https://www.baidu.com/s?wd=westos
"""
import requests

def keyword_post(url, data):
    try:
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
        response = requests.get(url, params=data, headers={'User-Agent': user_agent})
        response.raise_for_status()   # 如果返回的状态码不是200， 则抛出异常;
        response.encoding = response.apparent_encoding  # 判断网页的编码格式， 便于respons.text知道如何解码;
    except Exception as e:
        print("爬取错误")
    else:

        print(response.url)
        print("爬取成功!")
        return  response.content




def baidu():
    url = "https://www.baidu.com"
    keyword = input("请输入搜索的关键字:")
    # wd是百度需要
    data = {
        'wd': keyword
    }
    keyword_post(url, data)


def search360():
    url = "https://www.so.com"
    keyword = input("请输入搜索的关键字:")
    # wd是百度需要
    data = {
        'q': keyword
    }
    content = keyword_post(url, data)

    with open('360.html', 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    search360()
