"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import socket
import select

sk1 = socket.socket()
sk1.bind(('0.0.0.0', 8001))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(('0.0.0.0', 8002))
sk2.listen(5)

sk3 = socket.socket()
sk3.bind(('0.0.0.0', 8003))
sk3.listen(5)

inputs = [sk1, sk2, sk3, ]

while True:
    r_list, w_list, e_list = select.select(inputs,[],inputs,1)
    for sk in r_list:
        # conn?????????
        conn, address = sk.accept()
        conn.sendall(bytes('hello', encoding='utf-8'))
        conn.close()

    for sk in e_list:
        inputs.remove(sk)