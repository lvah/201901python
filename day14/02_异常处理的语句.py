"""
try......except... else......finally......


"""
# 普通的异常处理：
# import  time
# try:
#     # 如果你觉得代码可能出现问题， 那么放在try语句中， 只执行一次；
#     print(s)
#     # print("hello")
# except NameError as e:   # 对于异常进行一个重命名；记录了异常的详细信息；
#     # 可能执行一次， 也可能不执行；
#     print("名称错误")
#     with open("except.log", 'w') as f:
#         f.write(time.ctime() + ' ')
#         f.write(str(e))
# finally:
#     # 无论是否出现异常， 肯定会执行一次，
#     print("处理结束")


import  time
try:
    # 如果你觉得代码可能出现问题， 那么放在try语句中， 只执行一次；
    print('hello')
    with open('/etc/aa') as f:
        print(f.read()[:5])

    print("文件读取结束")
    li = [1, 2, 3, 4]   # try语句中一旦出现问题， 后面的语句(try里面的)不执行
    print(li[5])
    print(s)
    print("hello")
except (NameError, IndexError) as e:   # 对于异常进行一个重命名；记录了异常的详细信息；
    # 可能执行一次， 也可能不执行；
    # print("名称错误")
    with open("except.log", 'a+') as f:
        f.write(time.ctime() + ' ' + str(e) + '\n')
finally:
    # 无论是否出现异常， 肯定会执行一次，
    print("处理结束")



