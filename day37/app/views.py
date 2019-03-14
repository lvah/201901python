"""
文件名: $NAME.py
日期: 10  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

# 存储视图函数的部分

"""


# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/
from flask import render_template

from app import app
from app.models import User


@app.route('/list/')
@app.route('/list/<int:page>/')
def list(page=1):
    # 每页显示的数据
    per_page = 10
    # 返回的是 Pagination对象
    userPageObj = User.query.paginate(page=page, per_page=per_page)
    return render_template('list.html',
                           userPageObj=userPageObj
                           )


