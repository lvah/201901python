"""
文件名: .py
创建时间: 2019-01-16 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException
def connect(cmd, hostname, user, password):
    import paramiko
    # ssh root@172.25.254.250
    # 创建一个ssh对象;
    client = paramiko.SSHClient()
    # 2. 解决问题:如果之前没有；连接过的ip, 会出现
    # Are you sure you want to continue connecting (yes/no)? yes
    # 自动选择yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 3. 连接服务器
        client.connect(
            hostname=hostname,
            username=user,
            password=password
        )
    except NoValidConnectionsError as e:
        return  "主机%s连接失败" %(hostname)
    except AuthenticationException as e:
        return "主机%s密码错误" % (hostname)
    except Exception as e:
        return  "未知错误: ", e
    else:
        # 4. 执行操作
        stdin, stdout, stderr = client.exec_command('hostname')
        # 5. 获取命令的执行结果;
        res = stdout.read().decode('utf-8')
        # 6. 关闭连接
        client.close()

        return  res


if __name__ == '__main__':
    with open('doc/hosts.txt') as f:
        for line in f:
            # 172.25.254.1:root:westos
            hostname, username, password = line.strip().split(":")
            res = connect('hostname', hostname, username, password )
            print(hostname.center(50, '*'))
            print("主机名:", res)
