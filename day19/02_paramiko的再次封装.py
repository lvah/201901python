# ssh远程连接集成了执行命令， 上传文件和下载文件的类;
import os
import sys

import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException, SSHException
import logging

logging.basicConfig(filename='my.log', level=logging.WARN,
                    format="%(asctime)s-%(filename)s-%(lineno)d- %(levelname)s: %(message)s ")


class SshRemoteHost(object):
    """
    1). 实现类似lftp的功能， 只支持一部分的命令， 输入的命令不存在， 则报错；
    """

    def __init__(self, host, user, pwd, cmd, port=22):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.cmd = cmd  # cmd hostname;   cmd ls -l; cmd data +%F

    def run(self):
        # cmd hostname  类的反射机制
        cmd_str = self.cmd.split()[0]  # cmd
        if hasattr(self, 'do_' + cmd_str):  # 判断是否有do_cmd方法
            getattr(self, 'do_' + cmd_str)()
        else:
            logging.error("目前不支持该操作.....目前支持cmd, put, get")
            print("目前不支持该操作.....目前支持cmd, put, get")

    def do_cmd(self):
        print("正在执行命令......")
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
                hostname=self.host,
                username=self.user,
                password=self.pwd
            )
        except NoValidConnectionsError as e:
            logging.error("主机%s连接失败" % (self.host))
            print("主机%s连接失败" % (self.host))
        except AuthenticationException as e:
            logging.error("主机%s密码错误" % (self.host))
            print("主机%s密码错误" % (self.host))
        except Exception as e:
            logging.error("未知错误: ", e)
            print("未知错误: ", e)
        else:
            # cmd hostname;   cmd ls -l; cmd data +%F
            #  ['cmd', 'ls',  '-l']
            # ['ls', '-l']
            # 'ls -l'
            cmd = " ".join(self.cmd.split()[1:])
            # 4. 执行操作
            stdin, stdout, stderr = client.exec_command(cmd)
            # 5. 获取命令的执行结果;
            res = stdout.read().decode('utf-8')
            logging.debug("%s 主机执行命令%sd的结果: %s" % (
                self.host, self.cmd, res))
            # 6. 关闭连接
            client.close()
            print(res)

    def do_put(self):
        """
        put /etc/passwd  /tmp/hello
        :return:
        """
        print('正在批量上传文件.....')
        # 类似于sftp命令的功能
        try:

            # 建立与远程主机的通道；
            transport = paramiko.Transport((self.host, int(self.port)))
            # 验证用户名和密码是否正确；
            transport.connect(username=self.user, password=self.pwd)
            # 根据创建并验证成功的通道， 创建sftp客户端;
        except AuthenticationException as e:
            logging.error("%s 密码错误" %(self.host),)
            print("%s 密码错误:" %(self.host), e)
        except SSHException as e:
            logging.error("%s未知错误   :" % (self.host))
            print('unknown error:', e)

        else:
            sftp = paramiko.SFTPClient.from_transport(transport)

            # 上传文件
            # put file1 file2
            filenames = self.cmd.split()[1:]
            if len(filenames) == 2:
                # 如果执行命令: put /etc/passwd /tmp/passwd
                # 目标主机上有文件: /tmp/passwd_172.25.254.1
                print(filenames[0], filenames[1]+'_'+self.host)
                sftp.put(filenames[0], filenames[1] + '_' + self.host)

            else:
                print("命令错误, 用法: put 源文件名 目标文件名")

                # 关闭两台主机建立的通道;
                transport.close()

    def do_get(self):
        print('正在批量下载文件.....')
        # 类似于sftp命令的功能
        try:

            # 建立与远程主机的通道；
            transport = paramiko.Transport((self.host, int(self.port)))
            # 验证用户名和密码是否正确；
            transport.connect(username=self.user, password=self.pwd)
            # 根据创建并验证成功的通道， 创建sftp客户端;

        except SSHException as e:
            logging.error("%s未知错误   :" % (self.host), e)
            # print("%s未知错误:" % (self.host), e)
            print('unknown error:', e)

        else:
            sftp = paramiko.SFTPClient.from_transport(transport)

            # 上传文件
            # put file1 file2
            filenames = self.cmd.split()[1:]
            if len(filenames) == 2:
                # 如果执行命令: put /etc/passwd /tmp/passwd
                # 目标主机上有文件: /tmp/passwd_172.25.254.1
                print(filenames[0], filenames[1]+'_'+self.host)
                sftp.get(filenames[0], filenames[1] + '_' + self.host)

            else:
                print("命令错误, 用法: put 源文件名 目标文件名")

                # 关闭两台主机建立的通道;
                transport.close()



def main():
    CONFDIR = 'conf'
    # 1. 主机组显示:
    print("主机组显示:".center(50, '*'))
    # 如何获取conf目录中主机的分组(遍历conf目录中的所有以.conf结尾的文件，主机组名需要去掉.conf);
    groups = [file.rstrip('.conf') for file in os.listdir(CONFDIR) if file.endswith('.conf')]
    for group in groups: print('\t', group)

    while True:
        choiceGroup = input("请选择操作的主机组名称(eg: web):")
        if choiceGroup not in groups:
            logging.error("%s不存在" % (choiceGroup))
            print("%s不存在" % (choiceGroup))
        else:
            break

    # 2. 根据选择的主机组， 显示包含的主机IP/主机名;
    #   1). 打开对应主机的配置文件, eg: conf/mysql.conf
    #   2). 依次读取文件的每一行， 获取主机名;
    infostr = "%s主机组包含的主机:" % (choiceGroup)
    print(infostr.center(50, '*'))
    hostinfos = []  # 存储需要操作的主机信息
    with open('%s/%s.conf' % (CONFDIR, choiceGroup)) as f:
        for line in f:
            # 172.25.254.6:22:root:westos
            # print(line.split(":")[0])
            hostinfos.append(line.strip().split(':'))

            hostname, port, user, passwd = line.strip().split(':')
            print(hostname)

    #  3. 批量执行脚本
    print("批量执行脚本".center(50, '*'))
    while True:
        cmd = input(">>: ")
        if cmd:
            if cmd in ['exit', 'quit']:
                print("执行结束， 退出中.......")
                sys.exit(0)
            else:
                # cmd, put, get
                for host in hostinfos:
                    hostname, port, user, passwd = host
                    print(hostname.center(50, '*'))
                    sshObj = SshRemoteHost(hostname, user, passwd, cmd, port)
                    sshObj.run()


if __name__ == '__main__':
    main()
