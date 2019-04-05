"""
文件名: utils.py
日期: 2019-03-24  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from functools import wraps

from flask import session, flash, redirect, url_for, request, abort

from app import db
from app.models import AdminOplog, Admin, Auth


def is_admin_login(f):
    """用来判断用户是否登录成功"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 判断session对象中是否有seesion['admin'],
        # 如果包含信息， 则登录成功， 可以访问主页；
        # 如果不包含信息， 则未登录成功， 跳转到登录界面;；
        if session.get('admin', None):
            return f(*args, **kwargs)
        else:
            flash("管理员必须登录才能访问%s" % (f.__name__))
            return redirect(url_for('admin.login'))

    return wrapper


def permission_control(f):
    """判断管理员是否有权限操作，（如果是超级管理员， 则全部可以操作） 如果没有权限抛出403"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        admin = Admin.query.get_or_404(session.get('admin_id'))
        if not admin.is_super:  # 如果不是超级用户， xxxx
            # 获取当前用户拥有的权限, 默认是字符串'1,2,3'
            auths = admin.role.auths
            # 获取所有的权限列表;
            all_auth = Auth.query.all()
            # 管理员可以访问的权限id号
            auths = map(int, auths.split(','))

            # 获取管理员可以访问的路由地址
            admin_urls = [Auth.query.get_or_404(id).url for id in auths]
            print("管理员可以访问的路由地址:", admin_urls)
            print("管理员正在访问的url路由地址:", request.url_rule)
            print(request.url)
            if str(request.url_rule) not in admin_urls:
                # Flask抛出异常， 403代表permission deny
                abort(403)
        return f(*args, **kwargs)

    return wrapper


def write_adminlog(content):
    """将操作日志写入数据库中"""
    adminOplog = AdminOplog(
        admin_id=session.get('admin_id'),
        content=content,
        ip=request.remote_addr
    )
    db.session.add(adminOplog)
    db.session.commit()
