# 棋盘向左移动?
#  1). 只要棋盘的每一行可以向左移动， e；
#          目标: 如何让棋盘的每一行向左移动?
#           [2， 2， 2， 2] === [4, 4, 0 ,0 ]
#           讨论:
#               1). 先把这一行的非0 数字向前放， 0向后放；   ==== [2, 2, 2, 2]
#               2). 依次循环判断两个数是否相等， 如果相等， 第一个*2， 第二个数为0；  【4， 0， 4， 0】
#               3).先把这一行的非0数字向前放， 0向后放；[4, 4, 0 ,0 ]


score = 0
def invert(field):
    """矩阵的反转"""
    return  [row[::-1] for row in field]

def transpose(field):
    """实现矩阵的转置"""
    # zip: 实现
    # *field对列表进行解包;
    return  list(zip(*field))


# 1). 先把这一行的非0 数字向前放， 0向后放；   ==== [2, 2, 2, 2]
def tight(row):  # [2,0,2,0]
    return sorted(row, key=lambda x: 1 if x == 0 else 0)


# 2). 依次循环判断两个数是否相等， 如果相等， 第一个*2， 第二个数为0；  【4， 0， 4， 0】
def merge(row):
    for index in range(3):
        if row[index] == row[index + 1]:
            row[index] *= 2
            row[index + 1] = 0
            # 如果合并完成， 分数增加row[index]
            global score
            score += row[index]
    return row


def move_row_left(row):
    return tight(merge(tight(row)))

def move_left(field):
    return  [move_row_left(row) for row in field]

def move_right(field):
    field = invert(field)
    return  invert(move_left(field))

def move_up(field):
    field = transpose(field)
    return  transpose(move_left(field))


def move_down(field):
    field = transpose(field)
    return transpose(move_right(field))

if __name__ == '__main__':
    print(move_right([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]))
    print(move_right([[0, 0, 2, 2], [0, 2, 4, 4], [0, 2, 0, 0], [2, 2, 0, 4]]))
    print(move_up([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4]]))
    print(move_up([[0, 0, 2, 2], [0, 2, 4, 4], [0, 2, 0, 0], [2, 2, 0, 4]]))
    print(move_down([[0, 0, 2, 2], [0, 2, 4, 4], [0, 2, 0, 0], [2, 2, 0, 4]]))