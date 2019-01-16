"""
文件名: .py
创建时间: 2019-01-16 16:
作者: lvah
联系方式: 976131979@qq.com
代码描述:



目标:
    1). 172.25.254.3   - host3
        172.25.254.4   - host4

    2). host4实现无密码连接host3？



     *****host3操作: 生成公钥和私钥， 并发送私钥给host4
              993  ssh-keygen
              994  cd  /root/.ssh/
              995  ls
              996  ssh-copy-id  -i  id_rsa.pub root@172.25.254.3
              997  scp id_rsa kiosk@172.25.254.4:/home/kiosk/.ssh/


    *****host4操作：
    a). shell命令检测是否可以成功?
    ssh root@172.25.254.3

    b). 代码实现:
        import paramiko
        # ssh root@172.25.254.250
        # 创建一个ssh对象;
        client = paramiko.SSHClient()


        # 实例化一个私钥对象
        private_key = paramiko.RSAKey.from_private_key_file('/home/kiosk/.ssh/id_rsa')
        # 2. 解决问题:如果之前没有；连接过的ip, 会出现
        # Are you sure you want to continue connecting (yes/no)? yes
        # 自动选择yes
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 3. 连接服务器
        client.connect(
            hostname='172.25.254.3',
            username='root',
            pkey= private_key ,

        )
        # 4. 执行操作
        stdin, stdout, stderr = client.exec_command('hostname')
        # 5. 获取命令的执行结果;
        print(stdout.read().decode('utf-8'))
        # 6. 关闭连接
        client.close()


"""


import paramiko
# ssh root@172.25.254.250
# 创建一个ssh对象;
client = paramiko.SSHClient()


# 实例化一个私钥对象
private_key = paramiko.RSAKey.from_private_key_file('doc/id_rsa')
# 2. 解决问题:如果之前没有；连接过的ip, 会出现
# Are you sure you want to continue connecting (yes/no)? yes
# 自动选择yes
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 3. 连接服务器
client.connect(
    hostname='172.25.254.3',
    username='root',
    pkey= private_key ,

)
# 4. 执行操作
stdin, stdout, stderr = client.exec_command('hostname')
# 5. 获取命令的执行结果;
print(stdout.read().decode('utf-8'))
# 6. 关闭连接
client.close()
