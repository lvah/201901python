import paramiko
from paramiko import AuthenticationException, SSHException
import logging

def put(hostname, password, source_name, target_name):
    # 类似于sftp命令的功能
    try:
        # 建立与远程主机的通道；
        transport = paramiko.Transport(('172.25.254.4', 22))
        # 验证用户名和密码是否正确；
        transport.connect(username='root', password='Asimov')
        # 根据创建并验证成功的通道， 创建sftp客户端;
        sftp = paramiko.SFTPClient.from_transport(transport)
    except AuthenticationException as e:
        print("密码错误:", e)
    except SSHException as e:
        print("主机不存在:", e)
    except Exception as e:
        print("未知错误:", e)
    else:
        # 上传文件
        # sftp.put('/etc/passwd', '/mnt/172.25.254.250')
        # 下载文件;
        sftp.get('/mnt/172.25.254.250')
    finally:
        # 关闭两台主机建立的通道;
        transport.close()
