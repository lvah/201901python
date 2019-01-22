"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
# 实现http客户端的程序， 获取百度页面
import socket
# http://www.baidu.com:80
# 实例化socket对象; 默认参数指定为IPv4协议， 和TCP传输协议;
client = socket.socket()
# 连接服务器端
client.connect(('www.baidu.com', 80))
# 给百度服务器发送请求通过GET方法请求主页内容的请求， http协议的版本为1.1;
client.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')
# 接收服务端返回的页面内容;
recvData = client.recv(1024*100)
# 解码为能够识别的字符串;
print(recvData.decode('utf-8'))
# 关闭客户端连接;
client.close()