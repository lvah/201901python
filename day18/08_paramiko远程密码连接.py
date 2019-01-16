"""
文件名: .py
创建时间: 2019-01-16 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:

# paramiko是什么? 基于ssh用于连接远程服务器做操作:远程执行命令， 上传文件， 下载文件
"""

import paramiko
# ssh root@172.25.254.250
# 创建一个ssh对象;
client = paramiko.SSHClient()
# 2. 解决问题:如果之前没有；连接过的ip, 会出现
# Are you sure you want to continue connecting (yes/no)? yes
# 自动选择yes
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 3. 连接服务器
client.connect(
    hostname='172.25.254.1',
    username='root',
    password='westos'
)
# 4. 执行操作
stdin, stdout, stderr = client.exec_command('hostname')
# 5. 获取命令的执行结果;
print(stdout.read().decode('utf-8'))
# 6. 关闭连接
client.close()
