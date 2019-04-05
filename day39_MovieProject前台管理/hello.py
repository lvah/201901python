"""
文件名: hello.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import json

import requests


def getAddrByIp(ip):
    url = "http://ip.taobao.com/service/getIpInfo.php"
    data = {
        'ip': ip
    }
    response = requests.get(url, params=data)
    content = json.loads(response.text)
    country = content['data']['country']
    city = content['data']['city']
    return country + city

print(getAddrByIp('127.0.0.1'))