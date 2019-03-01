"""
文件名: $NAME.py
日期: 28  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from _curses import flash
from functools import wraps
from flask import session, redirect, url_for


def is_login(f):
    """用来判断用户是否登录成功"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 判断session对象中是否有seesion['user'],
        # 如果包含信息， 则登录成功， 可以访问主页；
        # 如果不包含信息， 则未登录成功， 跳转到登录界面;；
        if session.get('user', None):
            return f(*args, **kwargs)
        else:
            flash("用户必须登录才能访问%s" % (f.__name__))
            return redirect(url_for('login'))

    return wrapper
