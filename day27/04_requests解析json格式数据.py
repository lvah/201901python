"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import json
import requests


# 解析json格式
ip = input('IP:')
url = "http://ip.taobao.com/service/getIpInfo.php"
data = {
    'ip': ip
}
response = requests.get(url, params=data)
# 将响应的json数据编码为python可以识别的数据类型;
content = response.json()
print(content)
print(type(content))
country = content['data']['country']
print(country)


#  response.content: 返回的是bytes类型， 比如： 下载图片， 视频；
#  response.text: 返回的是str类型， 默认情况会将bytes类型转成str类型;
