import os
import shlex
import sys
import time
from subprocess import Popen, PIPE

jms_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(jms_dir)


def bash(cmd):
    """
    run a bash shell
    执行bash命令
    """
    with Popen(shlex.split(cmd), stdout=PIPE) as proc:
        return proc.stdout.read().decode('utf-8')


def valid_ip(ip):
    if ('255' in ip) or (ip == '0.0.0.0'):
        return False
    else:
        return True


def color_print(msg, color='red', exist=False):
    """
    print colorful string
    颜色打印字符或者退出
    """
    color_msg = {
        'blue': '\033[1;36m%s\033[0m',
        'green': '\033[1;32m%s\033[0m',
        'yellow': '\033[1;33m%s\033[0m',
        'red': '\033[1;31m%s\033[0m',
        'title': '\033[30;42m%s\033[0m',
        'info': '\033[32m%s\033[0m',

    }


    msg = color_msg.get(color, 'red') %(msg)
    print(msg)
    if exist:
        time.sleep(2)
        sys.exit()
    return  msg


# print(bash('ls -a /home/kiosk/'))
color_print('hello', 'yellow')