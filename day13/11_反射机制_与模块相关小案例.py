"""



"""

from lib import  bbs

def run():

    # 用户输入url地址： http://www.baidu.com/news/index
    # 用户输入url地址： http://www.baidu.com/bbs/login
    modules, func = input('url:').split('/')[-2:]  # 获取目录的倒数两个， 即 bbs login
    # print(modules, func)
    # 倒入一个包含变量的模块名， 其中obj就是导入模块的别名
    obj = __import__('lib.'+  modules)
    # print(obj)
    if hasattr(obj, func):
        return getattr(obj, func)()
    else:
        return '404:页面找不到'

if __name__ == '__main__':
    while True:
        print(run())
