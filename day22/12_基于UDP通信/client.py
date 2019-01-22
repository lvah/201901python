"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import socket

udpClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpClient.sendto(b'hello server', ('172.25.254.250', 9001))
recvData, address = udpClient.recvfrom(1024)
print("接收服务端的数据: ", recvData.decode('utf-8'))
udpClient.close()


