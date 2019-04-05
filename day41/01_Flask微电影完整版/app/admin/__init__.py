from flask import  Blueprint


# Blueprint接受两个参数实例化，分别为蓝本的名字和蓝本所在的包或模块，
# 大多数情况下第二个参数使用Python 的__name__ 变量即可。
admin =  Blueprint("admin", __name__)

from app.admin.views.main import  *
from app.admin.views.tag import  *
from app.admin.views.movie import  *
from app.admin.views.preview import *
from app.admin.views.user import *
from app.admin.views.comment import *
from app.admin.views.collect import *
from app.admin.views.logs import *
from app.admin.views.auth import *
from app.admin.views.role import *
from app.admin.views.admin import *

# 比悲伤更悲伤的故事
