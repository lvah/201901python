"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from urllib.error import URLError
from urllib.request import urlopen
from urllib import  request

url = "http://www.cbrc.gov.cn/chinese/jrjg/index.html"
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
reqObj = request.Request(url, headers={'User-Agent': user_agent})
content = urlopen(reqObj).read().decode('utf-8')
print(content)