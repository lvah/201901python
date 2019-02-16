"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


import requests
from bs4 import BeautifulSoup

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
    # 提取页面的头部信息， 解决乱码问题
    headObj = soup.head

    # 提取需要的内容;
    divObj = soup.find_all('div', class_="blog-content-box")[0]

    #
    scriptObj = soup.script
    with open('doc/csdn.html', 'w') as f:
        # 写入头部信息(指定编码格式和标题)
        f.write(str(headObj))
        # 写入博客正文;
        f.write(str(divObj))
        print("下载成功......")

        # f.write(str(scriptObj))
if __name__ == '__main__':
    url = "https://blog.csdn.net/King15229085063/article/details/87380182"
    content = get_content(url)
    parser_content(content)
