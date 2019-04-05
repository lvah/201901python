from flask import  Blueprint


# Blueprint接受两个参数实例化，分别为蓝本的名字和蓝本所在的包或模块，
# 大多数情况下第二个参数使用Python 的__name__ 变量即可。
admin =  Blueprint("admin", __name__)

from app.admin.views import  *



