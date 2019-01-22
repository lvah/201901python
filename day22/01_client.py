"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

content = str(obj.recv(1024), encoding='utf-8')
print(content)

obj.close()

# ???c2.py
import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8002))

content = str(obj.recv(1024), encoding='utf-8')
print(content)

obj.close()