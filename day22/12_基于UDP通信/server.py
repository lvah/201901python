"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
# 实现: udp多个客户端可以连接服务端， 发送命令， 返回的是命令的执行结果;

import socket


# 1. 实例化socket对象
udpServer = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
# 2. 绑定IP和端口
# 172.25.254.250
# 0.0.0.0代表开放所有的IP地址
udpServer.bind(('0.0.0.0', 9001))

print("等待客户端UDP的连接.....")

# 3. 接收客户端的连接
recvdata, address = udpServer.recvfrom(1024)
print("接收到客户端的数据: ", recvdata.decode('utf-8'))
# 4. 给客户端回复消息
udpServer.sendto(b"hello client", address)

# 5. 关闭socket对象
udpServer.close()



