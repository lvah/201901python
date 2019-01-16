"""
文件名: .py
创建时间: 2019-01-16 10:
作者: lvah
联系方式: 976131979@qq.com
代码描述:



  本来是想通过这个案例练习下正则表达式的，后来才发现有更简单的方法， 当然是网上有很多API接口， 直接可以返>回json格式的数据， 通过处理， easy搞定……

    根据IP查询所在地、运营商等信息的一些API如下：
    1. 淘宝的API（推荐）：http://ip.taobao.com/service/getIpInfo.php?ip=110.84.0.129
    2. 国外freegeoip.net（推荐）：http://freegeoip.net/json/110.84.0.129 这个还提供了经纬度信息（但不一定准>）
    3. 新浪的API：http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=110.84.0.129
    4. 腾讯的网页查询(返回的非json格式): http://ip.qq.com/cgi-bin/searchip?searchip1=110.84.0.129
    5. ip.cn的网页（返回的非json格式）：http://www.ip.cn/index.php?ip=110.84.0.129
    6. ip-api.com： http://ip-api.com/json/110.84.0.129

上述的API接口，大多有一个特点是， 返回的直接是个json格式;




# Json数据: JavaScript Object Notation, 一种轻量型数据交换格式， 便于阅读和交换数据.



"""
# 1. 简单的爬虫:
from urllib.request import urlopen

url = "http://ip-api.com/json/110.84.0.129"
urlObj = urlopen(url)

# 服务端返回的页面信息, 此处为字符串类型
pageContent = urlObj.read().decode('utf-8')
print(pageContent)
print(type(pageContent))

# 2. 处理Json数据
import json
# 解码: 将json数据格式解码为python可以识别的对象;
dict_data = json.loads(pageContent)
print(dict_data)
print(type(dict_data))

print("""
所在城市: %s
所在国家: %s

""" %(dict_data['city'], dict_data['country']))

