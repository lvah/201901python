"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


import requests



# # 1). 上传文件files: 指定的文件的内容
# data = {
#     'name':'fentiao'
# }
# files = {
#     # 二进制文件需要指定rb
#     'file': open('doc/movie.jpg', 'rb')
# }
# response = requests.post(url='http://httpbin.org/post', data = data, files=files)
# print(response.text)



# 2). 设置代理
# proxies = {
#     'http':'116.209.58.116:9999',
#     'https':'115.151.5.40:53128'
# }
# response = requests.get('http://httpbin.org/get', proxies=proxies, timeout=2)
# print(response.text)



# 3). cookie信息的保存， 加载====== 客户端的缓存， 保持客户端和服务端连接会话seesion
# seesionObj = requests.session()
# # 专门用来设置cookie信息的，
# response1 = seesionObj.get('http://httpbin.org/cookies/set/name/westos')
# # 专门用来查看cookie信息的网址
# response2 = seesionObj.get('http://httpbin.org/cookies')
# print(response2.text)


# 专门用来设置cookie信息的，
response1 = requests.get('http://httpbin.org/cookies/set/name/westos')
# 专门用来查看cookie信息的网址
response2 = requests.get('http://httpbin.org/cookies')
print(response2.text)




