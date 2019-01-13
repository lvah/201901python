# 1, 画它的分隔符
import random
def draw_sep():
    print("+-----" * 4 + '+')

# 2. 画每一行的格子
def draw_one_row(row):  # [0, 2, 0, 0]   |    |  2  |    |    |
    print("".join([ '|  %d  '%(item) if item != 0 else '|     ' for item in row ]) + '|')

# draw_one_row([0, 2, 0, 0])

# 3. 创建棋盘的数据， 默认情况下时4*4， 数值全为0；
field = [[0 for j in range(4)] for i in range(4)]
# print(field)

# 4. 开始游戏时， 棋盘数据会随机生成2或者4，
def random_create():
    # field[0][2] = 2
    while True:
        firstIndex = random.choice(range(4))
        secondIndex = random.choice(range(4))
        if field[firstIndex][secondIndex] == 0:
            value = random.choice([2, 4, 2, 2, 2])
            field[firstIndex][secondIndex] = value
            break

def game():
    random_create()
    random_create()
    print(field)
    for row in field:
        draw_sep()
        draw_one_row(row)
    draw_sep()


if __name__ == '__main__':
    game()