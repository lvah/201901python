"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import requests
from urllib.error import  HTTPError


def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果状态码不是200， 引发HttpError异常
        # 从内容分析出响应内容的编码格式
        response.encoding = response.apparent_encoding
    except HTTPError as e:
        print(e)
    else:
        print(response.status_code)
        # print(response.headers)
        # return  response.text   # 返回的是字符串
        return  response.content  # 返回的是bytes类型， 不进行解码


if __name__ == '__main__':
    url = 'https://item.jd.com/6789689.html'
    content = get_content(url)
    with open('doc/jingdong.html', 'wb') as f:
        f.write(content)



# 1. 京东商品页面信息的爬取;  https://item.jd.com/6789689.html
# 2. 亚马逊商品页面信息的爬取;https://www.amazon.cn/dp/B01ION3VWI

