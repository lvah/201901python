from flask import Blueprint

# Blueprint接受两个参数实例化，分别为蓝本的名字和蓝本所在的包或模块，
# 大多数情况下第二个参数使用Python 的__name__ 变量即可。
admin = Blueprint("admin", __name__)

from app.admin.views.main import *
from app.admin.views.tag import *
from app.admin.views.movie import *
from app.admin.views.preview import *
from app.admin.views.user import *
from app.admin.views.comment import *
from app.admin.views.collect import *
from app.admin.views.logs import *
from app.admin.views.auth import *
from app.admin.views.role import *
from app.admin.views.admin import *


@admin.errorhandler(404)
def page_not_found(error):
    return render_template('admin/404.html'), 404


@admin.errorhandler(500)
def server_error(error):
    return render_template('admin/500.html'), 500


@admin.errorhandler(403)
def no_permission(error):
    return render_template('admin/403.html'), 403
