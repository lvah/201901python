"""
Assert statements are a convenient way to insert debugging assertions into a program:
assert语句是一种插入调试断点程序的一种便捷的方式。

assert语句的使用格式
        assert expression

这个语句是等价于下面的个句式:

        if __debug__:
            if not expression: raise AssertionError
"""


# age = int(input('Age:'))
# assert   0<age<120, "年龄不合法"


def is_huiwen_num(num):
    snum = str(num)
    return snum == snum[::-1]



def is_prime(num):  # 1 2
    assert  num  > 1
    from math import  sqrt
    for i in range(2, int(sqrt(num)+1)):
        if num % i  == 0:
            return  False
    else:
        return  True


if __name__ == '__main__':
    # try:
    #     assert is_huiwen_num(101) == True, 'Error'
    #     assert is_huiwen_num(1001) == True, 'Error'
    #     assert is_huiwen_num(101) == False, 'Error'
    # except AssertionError as e:
    #     print(e)
    # else:
    #     print("测试用例全部通过...")


    try:

        for num in [3,7,11,13]:
            assert is_prime(num) == True, ' %s Error' %(num)
        for num in [12,20,99999,132]:
            assert is_prime(num) == False, ' %s Error' %(num)

    except AssertionError as e:
        print(e)
    else:
        print("测试用例全部通过...")
