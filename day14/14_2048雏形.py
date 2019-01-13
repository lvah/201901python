import curses
import random
from itertools import chain


class GameField(object):
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        self.score = 0      # 当前得分
        self.highscore = 0   # 最高分


    # 重置棋盘， 重新开始游戏时， 执行的操作;
    def reset(self):
        # 2). 是否要更新最高分, 当前分数为0；
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0

        # 3). 创建棋盘的数据， 默认情况下时4*4， 数值全为0；
        self.field = [[0 for j in range(4)] for i in range(4)]

        self.random_create()
        self.random_create()


    # 开始游戏时， 棋盘数据会随机生成2或者4，
    def random_create(self):
        # field[0][2] = 2
        while True:
            firstIndex = random.choice(range(4))
            secondIndex = random.choice(range(4))
            if self.field[firstIndex][secondIndex] == 0:
                value = random.choice([2, 4, 2, 2, 2])
                self.field[firstIndex][secondIndex] = value
                break



    # 画棋盘
    def draw(self, stdstr):
        def draw_sep():
            # print("+-----" * 4 + '+')
            stdstr.addstr("+-----" * 4 + '+' + '\n')
        # 2. 画每一行的格子
        def draw_one_row(row):  # [0, 2, 0, 0]   |    |  2  |    |    |
            stdstr.addstr("".join(['|  %d  ' % (item) if item != 0 else '|     ' for item in row]) + '|\n')
        # 3. 绘制棋盘
        for row in self.field:
            draw_sep()
            draw_one_row(row)
        draw_sep()
        stdstr.addstr("\n当前分数: %s" %(self.score))
        stdstr.addstr("\n当前最高分数: %s" %(self.highscore))
        stdstr.addstr(" \n游戏帮助: 上下左右键  (R)estart Q(uit) ")
        if self.is_win():
            stdstr.addstr("\n游戏胜利\n")
        if self.is_gameover():
            stdstr.addstr("游戏失败\n")

    def is_win(self):
        return max(chain(*self.field)) >= 2048

    def is_gameover(self):
        return not any([self.is_move_left(self.field),
                        self.is_move_right(self.field),
                        self.is_move_up(self.field),
                        self.is_move_down(self.field) ])

    @staticmethod
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

    def is_move_left(self, field):
        # 只要棋盘的任意一行可以向左移动， 就返回True；
        return any([self.is_row_left(row) for row in  field])

    def invert(self, field):
        """矩阵的反转"""
        return [row[::-1] for row in field]

    def is_move_right(self, field):
        # 对棋盘的每一行元素进行反转;
        invertField = self.invert(field)
        return self.is_move_left(invertField)

    def transpose(self, field):
        """实现矩阵的转置"""
        # zip: 实现
        # *field对列表进行解包;
        return list(zip(*field))

    def is_move_up(self, field):
        # 对棋盘的每一行元素进行转置;
        transposeField = self.transpose(field)
        return self.is_move_left(transposeField)

    def is_move_down(self, field):
        # 判断能否向下移动, 也就是对于元素进行转置, 判断转置后的棋盘能否向右移动;
        # 对棋盘的每一行元素进行反转;
        transposeField = self.transpose(field)
        return self.is_move_right(transposeField)


def main(stdstr):
    game_field = GameField()
    game_field.reset()
    game_field.draw(stdstr)
    action = stdstr.getch()

curses.wrapper(main)