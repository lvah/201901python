"""
文件名: views.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
# 导入home的蓝图对象
import json

import requests

from app.home.forms import LoginForm

from . import home
from flask import render_template, flash, session, redirect, url_for, request
from werkzeug.security import generate_password_hash


@home.route('/')
def index():
    return render_template('home/base.html')


# def getAddrByIp(ip):
#     url = "http://ip.taobao.com/service/getIpInfo.php"
#     data = {
#         'ip': ip
#     }
#     response = requests.get(url, params=data)
#     content = json.loads(response.text)
#     country = content['data']['country']
#     city = content['data']['city']
#     return country + city


@home.route('/login/', methods=['POST', 'GET'])
def login():
    from app.models import User, Userlog
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(name=username).first()
        if user and user.verify_password(password):
            # session信息的保存
            session['user_id'] = user.id
            session['user'] = user.name
            flash("用户%s登录成功" % (user.name))
            remote_ip = request.remote_addr
            Userlog(user_id=user.id,
                    ip=remote_ip,
                    area='xxx内网IP')
            # 从index蓝图里面寻找index函数;
            return redirect(url_for('home.index'))
        else:
            flash("用户登录失败")
            return redirect(url_for('home.login'))
    return render_template('home/login.html',
                           form=form)
