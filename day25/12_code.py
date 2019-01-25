"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



问题描述:
    北美电话的常用格式:(eg: 2703877865)
            前3位: 第一位是区号以2~9开头 , 第2位是0~8, 第三位数字可任意;
            中间三位数字:第一位是交换机号, 以2~9开头, 后面两位任意
            最后四位数字: 数字不做限制;



1234567890
123-456-7890
123.456.7890
123 456 7890
(123) 456 7890


# 转义的实现:
#   + , ? , (), *, . 一定要转义
# () ---有自己的用法， 对()进行转义
# . ---有自己的用法， 对。进行转义
"""
import random
import re
import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s执行时间: %fs" % (f.__name__, end_time - start_time))
        return res

    return wrapper




def createPhone():
    with open('phoneText.txt', 'w') as f:
        for i in range(1000000):
            # 生成一个随机的电话号码;
            phone = "".join([str(random.randint(0, 9)) for i in range(10)])
            f.write(phone + '\n')




@timeit
def use_compile():
    pattern = r"\(?[2-9][0-8]\d\)?[-\.\s]?[2-9]\d{2}[-\.\s]?\d{4}"
    compilePattern = re.compile(pattern)

    with open('phoneText.txt') as f:
        for line in f:
            phone = line.rstrip()
            res = re.search(compilePattern, phone)
            if res:
                # print(res[0])
                return True
            return False


@timeit
def no_compile():
    pattern = r"\(?[2-9][0-8]\d\)?[-\.\s]?[2-9]\d{2}[-\.\s]?\d{4}"
    # pattern = r'\d{10}'
    with open('phoneText.txt') as f:
        for line in f:
            phone = line.rstrip()
            res = re.search(pattern, phone)
            if res:
                # print(res[0])
                return True
            return False


if __name__ == '__main__':
    # createPhone()
    no_compile()
    use_compile()

    # assert isPhone('1234567890') == True
    # assert isPhone('123-456-7890') == True
    # assert isPhone('123.456.7890') == True
    # assert isPhone('123 456 7890') == True
    # assert isPhone('(123) 456 7890') == True
