"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


# 1. 什么是爬虫?
就是在互联网上一直爬行的蜘蛛， 如果遇到需要的资源， 那么它就会抓取下来(html内容);
模拟浏览器快速访问页面的内容.



# 2. 浏览网页的过程中发生了什么?
- 浏览器输入http://www.baidu.com/bbs/;
- 1). 根据配置的DNS获取www.baidu.com对应的主机IP；
- 2). 根据端口号知道跟服务器的那个软件进行交互。
- 3). 百度的服务器接收客户端请求:
- 4). 给客户端主机一个响应(html内容) ----- html, css, js
- 5). 浏览器根据html内容解释执行， 展示出华丽的页面;


</li>                                                                                                                                                                                                <li
style="margin: 0px 10px 0px 5px; width: 120px; float: left; height: 30px; display: inline;">
<a href="http://www.cfets-icap.com.cn/" target="_blank"  style="color:#08619D">
上海国际货币经纪公司
</a>
</li>

常见模拟浏览器的信息:
  1.Android
    Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
    Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    2.Firefox

    Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
    Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0
    3.Google Chrome

    Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
    Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19
    4.iOS
    Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3



"""
import random
import re

from urllib.request import urlopen, Request
from urllib.error import  URLError
def get_content(url):
    """获取页面内容， 反爬虫之模拟浏览器"""
    # 防止一个浏览器访问频繁被封掉;
    user_agents = [
        "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
    ]
    try:
        # reqObj = Request(url, headers={'User-Agent': user_agent})
        reqObj = Request(url)
        # 动态添加爬虫请求的头部信息， 可以在实例化时指定， 也可以后续通过add—header方法添加
        reqObj.add_header('User-Agent', random.choice(user_agents))
    except URLError as e:
        print(e)
        return  None
    else:
        content = urlopen(reqObj).read().decode('utf-8').replace('\t', ' ')
        return  content


def parser_content(content):
    """解析页面内容， 获取银行名称和官网URL地址"""
    pattern = r'<a href="(.*)" target="_blank"  style="color:#08619D">\s+(.*)\s+</a>'
    bankinfos = re.findall(pattern, content)
    if not bankinfos:
        raise  Exception("没有获取符合条件的信息")
    else:
        return  bankinfos

def main():
    url = "http://www.cbrc.gov.cn/chinese/jrjg/index.html"
    content = get_content(url)
    bankinfos = parser_content(content)
    with open('doc/bankinfo.txt', 'w') as f:
        # ('http://www.cdb.com.cn/', '国家开发银行\r')
        for bank in bankinfos:
            name = bank[1].rstrip()
            url = bank[0]
            # 根据正则判断银行的url地址是否合法， 如果合法才写入文件;
            pattern =  r'^((https|http|ftp|rtsp|mms)?:\/\/)\S+'
            if re.search(pattern, url):
                f.write('%s: %s\n' %(name, url))
            else:
                print("%s无官方网站" %(name))
        print("写入完成....")


if __name__ == '__main__':
    main()



