"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

浏览器---urllib
http --- 共享html页面, 文件给客户端

"""
import socket



def handler(clientObj):
    # 5. 接收客户端发送的请求
    recvData = clientObj.recv(1024)
    with open('hello.html', 'rb') as f:
        sendData = f.read()

    # 告诉浏览器http版本
    clientObj.send(b'HTTP/1.1 200 ok\r\n\r\n')
    clientObj.send(sendData)


def webServer():
    # 1. 创建socket对象
    server = socket.socket()
    # 2. 绑定端口和ip
    server.bind(('0.0.0.0', 8084))
    # 3. 监听是否有客户端连接
    server.listen(5)
    print("http服务正在启动8080........")


    while True:
        # 4. 接收客户端的连接
        clientObj, address = server.accept()
        t = threading.Thread(target=handler, args=(clientObj, ))
        t.start()

    server.close()
if __name__ == '__main__':
    webServer()


