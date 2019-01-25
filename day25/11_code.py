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


def isPhone(pattern, phone):
    """
    \(?             对(进行转义
    [2-9][0-8]\d    前3位: 第一位是区号以2~9开头 , 第2位是0~8, 第三位数字可任意;
    \)?             对)进行转义
    [-\.\s]?         中间位- . 空格任意一种， 并且可以省略;
    [2-9]\d{2}      中间三位数字:第一位是交换机号, 以2~9开头, 后面两位任意
    [-\.\s]?         中间位- . 空格任意一种， 并且可以省略;
    \d{4}            最后四位数字: 数字不做限制;

    """
    res = re.search(pattern, phone)
    if res:
        # print(res[0])
        return True
    return False


def createPhone():
    with open('phoneText.txt', 'w') as f:
        for i in range(10000):
            # 生成一个随机的电话号码;
            phone = "".join([str(random.randint(0, 9)) for i in range(10)])
            f.write(phone + '\n')

pattern = r"\(?[2-9][0-8]\d\)?[-\.\s]?[2-9]\d{2}[-\.\s]?\d{4}"
compilePattern = re.compile(pattern)
@timeit
def use_compile():
    with open('phoneText.txt') as f:
        for line in f:
            phone = line.rstrip()
            isPhone(compilePattern, phone)


@timeit
def no_compile():
    pattern = r"\(?[2-9][0-8]\d\)?[-\.\s]?[2-9]\d{2}[-\.\s]?\d{4}"
    with open('phoneText.txt') as f:
        for line in f:
            phone = line.rstrip()
            isPhone(pattern, phone)


if __name__ == '__main__':
    # createPhone()
    no_compile()
    use_compile()

    # assert isPhone('1234567890') == True
    # assert isPhone('123-456-7890') == True
    # assert isPhone('123.456.7890') == True
    # assert isPhone('123 456 7890') == True
    # assert isPhone('(123) 456 7890') == True
