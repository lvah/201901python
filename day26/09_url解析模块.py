"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


from urllib.parse import  urlencode
from urllib.parse import  urlparse



# data = urlencode({
#     'name': 'fentiao',
#     'password':'12345'
# })
# print(data)


# https://movie.douban.com/subject/4864908/comments?sort=time&status=P
# https://movie.douban.com/subject/4864908/comments?sort=new_score&status=P


# #**************** 对url地址进行编码
# data = urlencode({
#     'sort': 'time',
#     'status': 'P'
# })
# doubanUrl = 'https://movie.douban.com/subject/4864908/comments?' + data
# print(doubanUrl)




# #**************** 对url地址进行解析
doubanUrl = 'https://movie.douban.com/subject/4864908/comments?sort=new_score&status=P'
info = urlparse(doubanUrl)
print(info)
print(info.scheme)


