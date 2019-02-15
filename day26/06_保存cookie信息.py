"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




# 1. cookie信息是什么?

cookie某些网站为了辨别用户身份， 只有登陆某个页面才可以访问；
登陆信息保存方式: 进行一个会话跟踪(session),将用户的相关信息保存到本地的浏览器中;


# 2.


"""
from collections import Iterable
from urllib.parse import urlencode
from urllib.request import  HTTPCookieProcessor
from http import cookiejar
from urllib import request



#  **************************1. 获取cookie信息保存到变量**********************
# # CookieJar ------> FileCookieJar  ---> MozilaCookie
# # 1. 声明一个类， 将cookie信息保存到变量中;
# cookie = cookiejar.CookieJar()
#
# # 2. 通过urllib.request的 HTTPCookieProcessor创建cookie请求器；
# handler = HTTPCookieProcessor(cookie)
#
# # 3). 通过处理器创建opener; ==== urlopen
# opener = request.build_opener(handler)
#
# # 4). 打开url页面
# response = opener.open('http://www.baidu.com')
#
# # print(cookie)
# print(isinstance(cookie, Iterable))
# for item in cookie:
#     print("Name=" + item.name, end='\t\t')
#     print("Value=" + item.value)






#  **************************2. 获取cookie信息保存到本地文件**********************

# # 1). 指定年cookie文件存在的位置;
# cookieFilenName = 'doc/cookie.txt'
#
# # 2). 声明对象MozillaCookieJar, 用来保存cookie到文件中;
# cookie = cookiejar.MozillaCookieJar(filename=cookieFilenName)
#
#  # 3). 通过urllib.request的 HTTPCookieProcessor创建cookie请求器；
# handler = HTTPCookieProcessor(cookie)
#
# # 4). 通过处理器创建opener; ==== urlopen
# opener = request.build_opener(handler)
#
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# # 保存到本地文件中;
# cookie.save(cookieFilenName)



#  **********************************3. 从文件中获取cookie并访问********************************

# 1). 指定cookie文件存在的位置;
cookieFilenName = 'doc/cookie.txt'

# 2). 声明对象MozillaCookieJar, 用来保存cookie到文件中;
cookie = cookiejar.MozillaCookieJar()


# *****添加一步操作, 从文件中加载cookie信息
cookie.load(cookieFilenName)

 # 3). 通过urllib.request的 HTTPCookieProcessor创建cookie请求器；
handler = HTTPCookieProcessor(cookie)

# 4). 通过处理器创建opener; ==== urlopen
opener = request.build_opener(handler)

response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))




# **********************************4. 利用cookie模拟登陆网站的步骤**********************************


#  *******************88模拟登陆， 并保存cookie信息;
cookieFileName = 'cookie01.txt'
cookie = cookiejar.MozillaCookieJar(filename=cookieFileName)
handler = HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
#  这里的url是教务网站登陆的url;
loginUrl = 'xxxxxxxxxxxxxx'
postData = urlencode({
    'stuid': '1302100122',
    'pwd': 'xxxxxx'
})
response = opener.open(loginUrl, data=postData)
cookie.save(cookieFileName)

# bs4
# ******************8根据保存的cooie信息获取其他网页的内容eg: 查成绩/选课
gradeUrl = ''
response = opener.open(gradeUrl)
print(response.read())









