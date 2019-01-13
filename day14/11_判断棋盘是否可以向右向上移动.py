# 判断棋盘是否可以向右移动?
#   - 对棋盘的每一行元素进行反转, 判断反转后的棋盘能否向左一大批嗯, 也就是判断原有棋盘是否可以享有移动

from chess import  is_move_left

def invert(field):
    """矩阵的反转"""
    return  [row[::-1] for row in field]

def is_move_right(field):
    # 对棋盘的每一行元素进行反转;
    invertField = invert(field)
    return  is_move_left(invertField)

def transpose(field):
    """实现矩阵的转置"""
    # zip: 实现
    # *field对列表进行解包;
    return  list(zip(*field))

def is_move_up(field):
    # 对棋盘的每一行元素进行转置;
    transposeField = transpose(field)
    return  is_move_left( transposeField)


def is_move_down(field):
    # 判断能否向下移动, 也就是对于元素进行转置, 判断转置后的棋盘能否向右移动;
    # 对棋盘的每一行元素进行反转;
    transposeField = transpose(field)
    return is_move_right(transposeField)




if __name__ == '__main__':
    # print(invert([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]))
    # assert  is_move_right([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]) == True, 'Error'
    # print(transpose([[0, 2, 0, 2], [0, 2, 0, 0], [0, 0, 0, 0], [2, 0, 0, 4]]))
    assert  is_move_right([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]) == True, 'Error'
    print(is_move_right([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]))
