"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

1234567890
123-456-7890
123.456.7890
123 456 7890
(123) 456 7890


统一格式为:
            (123) 456-7890

"""


# 位置分组的使用
# import re
# def isPhone(phone):
#     pattern = r"\(?([2-9][0-8]\d)\)?[-\.\s]?([2-9]\d{2})[-\.\s]?(\d{4})"
#     res = re.search(pattern, phone)
#     if res:
#         info = res.groups()  # 返回的是元组
#         formatPhone = "(%s) %s-%s" %(info[0], info[1], info[2])
#         print(formatPhone)
#         return True
#     return False
#
# print(isPhone('777-777-7777'))
# print(isPhone('(777) 777 7890'))

# 命名分组的使用
import re
def isPhone(phone):
    pattern = r"\(?(?P<firstNum>[2-9][0-8]\d)\)?[-\.\s]?(?P<secondNum>[2-9]\d{2})" \
              r"[-\.\s]?(?P<thirdNum>\d{4})"
    res = re.search(pattern, phone)
    if res:
        info = res.groupdict()
        formatPhone = "(%s) %s-%s" %(info['firstNum'],
                                     info['secondNum'], info['thirdNum'])
        print(formatPhone)
        return True
    return False

print(isPhone('777-777-7777'))
print(isPhone('(777) 777 7890'))