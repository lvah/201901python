"""
文件名: views.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from . import  admin

from flask import  render_template
@admin.route('/')
def index():
    return  render_template('admin/base.html')


@admin.route('/login/')
def login():
    return  "后台登录"


