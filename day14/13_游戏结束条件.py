# 1. 何时用户游戏胜利?(当棋盘中出现num=2048时， 则代表用户胜利)
from itertools import  chain
field = [[2048, 0, 0, 0], [0, 0, 0, 0], [0, 0, 4, 0], [0, 0, 0, 4]]

def is_win(field):
    """
    list(chain(*[[2048, 0, 0, 0], [0, 0, 0, 0], [0, 0, 4, 0], [0, 0, 0, 4]]))
    [2048, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4]
    :param field:
    :return:
    """
    # 遍历所有的元素， 有一个元素大于等于2048， 即游戏胜利!
    # for row in field:
    #     for item in row:
    #         if item >= 2048:
    #             return  True
    # else:
    #     return  False
    return  max(chain(*field) >= 2048)
print(is_win(field))




# 2. 何时game over?(当用户在任何方向都不能移动时， 则代表游戏结束， 用户失败)
# 只要有任意一个方向可以移动， 那就没有结束
def is_over():
    return  not any([is_move_left(field),is_move_right(field),
                     is_move_up(field),is_move_down(field), ])
