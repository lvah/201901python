"""
文件名: $NAME.py
日期: 01  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


# 发送邮件的时候需要设置什么?
    - 发件人账户
    - 密码
    - 收件人
    - 邮件标题
    - 邮件正文
    - QQ邮件服务器的域名或者IP;



"""

from flask_mail import Mail, Message
from flask import Flask, render_template

app = Flask(__name__)

# 配置发送邮件的相关信息;
# 指定邮件服务器的域名或者IP
app.config['MAIL_SERVER'] = 'smtp.qq.com'

# 指定端口， 默认25， 但qq邮箱默认为 端口号465或587；
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '976131979'
# 此处的密码并非邮箱登录密码， 而是开启pop3
app.config['MAIL_PASSWORD'] = "个人密码"


def send_mail(to, subject, info):
    mail = Mail(app)
    msg = Message(subject=subject,
                  sender='976131979@qq.com',
                  recipients=to,
                  body=info
                  )
    with app.app_context():
        mail.send(msg)


send_mail(to=['976131979@qq.com', '2287236639@qq.com'], subject="第2次测试",
          info="邮件测试正文")

# if __name__ == '__main__':
#     app.run()
