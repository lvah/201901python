"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


import requests

# Http常见的请求方法:
#       GET:
#       post:

# 1.
# response = requests.get('http://www.baidu.com')
# print(response.text)

# 2.
# # http://httpbin.org/post
# response = requests.post('http://httpbin.org/post',
#               data={'name':'fentiao', 'age':10})
# print(response.text)


# 3.
# response = requests.delete('http://httpbin.org/delete', data={'name':'fentiao'})
# print(response.text)



# 4. GET方法：带参数get请求
# url1 = 'https://movie.douban.com/subject/4864908/comments?start=20&limit=20&sort=new_score&status=P'
url = 'https://movie.douban.com/subject/4864908/comments'
data = {
    'start':20,
    'limit':40,
    'sort':'new_score',
    'status': 'P'
}
response = requests.get(url, params=data)
print(response.text)
print(response.url)

