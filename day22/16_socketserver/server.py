"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

# 1. What is socketserver?

　    socket并不能多并发，只能支持一个用户，socketserver 简化了编写网络服务程序的任务，
socketserver是socket的在封装。socketserver在python2中为SocketServer,在python3
取消了首字母大写，改名为socketserver。socketserver中包含了两种类，一种为服务类（server
class），一种为请求处理类（request handle class）。前者提供了许多方法：像绑定，监听，运行……
（也就是建立连接的过程） 后者则专注于如何处理用户所发送的数据（也就是事务逻辑）。一般情况下，所有
的服务，都是先建立连接，也就是建立一个服务类的实例，然后开始处理用户请求，也就是建立一个请求处理类
的实例。

# 2. what types?
class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UnixDatagramServer(server_address, RequestHandlerClass,bind_and_activate=True)

# 3. How use socketserver?
　　1). 创建一个请求处理的类，并且这个类要继承 BaseRequestHandlerclass ，并且还要重写父类里handle()方法；
　　2). 你必须实例化 TCPServer，并且传递server IP和你上面创建的请求处理类，给这个TCPServer；
　　3). server.handle_requese()#只处理一个请求，server.server_forever()处理多个请求，永远执行
　　4). 关闭连接server_close()

# 4. Example?

"""

