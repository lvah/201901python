# 判断棋盘是否可以向左移动?
#  1). 只要棋盘的任意一行可以向左移动， 就返回True；
#          目标: 如何判断棋盘的一行是否可以向左移动?
#  2). 只要这一行的任意两个元素可以向左移动， 则返回True;
#           目标: 如何两个元素可以向左移动?
#           #  - 如果第一个数值为0， 第二个数值不为0， 则说明可以向左移动；
#           #  - 如果第一个数值不为0， 第二个数值与第一个元素相等， 则说明可以向左移动；


# True or False or True
# True
# any([True, False, True])
# True
# True and False and True
# False
# all([True, False, True])
# False


def is_row_left(row):  # [0, 2,2,0]
    # 任意两个元素可以向左移动？
    def is_change(index):  # index时索引值， [0,1,2,3]
        # - 如果第一个数值为0， 第二个数值不为0， 则说明可以向左移动；
        if row[index] == 0 and row[index + 1] != 0:
            return True
        # - 如果第一个数值不为0， 第二个数值与第一个元素相等， 则说明可以向左移动；
        if row[index] != 0 and row[index + 1] == row[index]:
            return True
        return False
    # 只要这一行的任意两个元素可以向左移动， 则返回True;
    return any([is_change(index) for index in range(3)])

def is_move_left(field):
    # 只要棋盘的任意一行可以向左移动， 就返回True；
    return any([is_row_left(row) for row in field])


if __name__ == "__main__":
    try:
        assert is_move_left([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]) == True, "棋盘向左移动失败"
        assert is_row_left([2, 2, 2, 2]) == True, 'Error'
        assert is_row_left([2, 4, 2, 4]) == False, 'Error'
    except AssertionError as e:
        print(e)
    else:
        print("测试用例完成.....")