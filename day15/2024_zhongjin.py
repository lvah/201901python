"""
文件名: .py
创建时间: 2019-01-05 16:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""

import curses
import random
from itertools import chain

class GameField(object):
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        self.score = 0      # 当前得分
        self.highscore = 0   # 最高分

        # 存储 判断各个方向是否可移动 的函数
        self.ismove = {}
        self.ismove['Left'] = self.is_move_left
        self.ismove['Right'] = self.is_move_right
        self.ismove['Up'] = self.is_move_up
        self.ismove['Down'] = self.is_move_down

        # 存储 执行各个方向移动 的函数
        self.moves = {}
        self.moves['Left'] = self.move_left
        self.moves['Right'] = self.move_right
        self.moves['Up'] = self.move_up
        self.moves['Down'] = self.move_down


    # 重置棋盘， 重新开始游戏时， 执行的操作;
    def reset(self):
        # 是否要更新最高分, 当前分数为0；
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0

        # 创建棋盘的数据， 默认情况下时4*4， 数值全为0；
        self.field = [[0 for j in range(4)] for i in range(4)]

        self.random_create()
        self.random_create()


    # 开始游戏时， 棋盘数据会随机生成2或者4，
    def random_create(self):

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
            stdstr.addstr("+-----" * 4 + '+' + '\n')

        # 画每一行的格子
        def draw_one_row(row):  # [0, 2, 0, 0]   |    |  2  |    |    |
            stdstr.addstr("".join(['|  %d  ' % (item) if item != 0 else '|     ' for item in row]) + '|\n')

        stdstr.clear()

        # 绘制棋盘
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
                        self.is_move_down(self.field)])

    @staticmethod
    def is_row_left(row):
        # 任意两个元素可以向左移动？
        def is_change(index):  # index时索引值
            # - 如果第一个数值为0， 第二个数值不为0， 则说明可以向左移动；
            if row[index] == 0 and row[index + 1] != 0:
                return True
            # - 如果第一个数值不为0， 第二个数值与第一个元素相等， 则说明可以向左移动；
            if row[index] != 0 and row[index + 1] == row[index]:
                return True
            return False

        # 只要这一行的任意两个元素可以向左移动， 则返回True;
        return any([is_change(index) for index in range(3)])


    def invert(self, field):
        """矩阵的反转"""
        return [row[::-1] for row in field]


    def transpose(self, field):
        """实现矩阵的转置"""
        # zip: 实现
        # *field对列表进行解包;
        return [list(row) for row in zip(*field)]


    def is_move_left(self, field):
        # 只要棋盘的任意一行可以向左移动， 就返回True；
        return any([self.is_row_left(row) for row in  field])


    def is_move_right(self, field):
        # 对棋盘的每一行元素进行反转;
        invertField = self.invert(field)
        return self.is_move_left(invertField)

    def is_move_up(self, field):
        # 对棋盘的每一行元素进行转置;
        transposeField = self.transpose(field)
        return self.is_move_left(transposeField)

    def is_move_down(self, field):
        # 判断能否向下移动, 也就是对于元素进行转置, 判断转置后的棋盘能否向右移动;
        # 对棋盘的每一行元素进行反转;
        transposeField = self.transpose(field)
        return self.is_move_right(transposeField)


    # 先把这一行的非零数向前放，零向后放 ==== [2,0,2,0]---->[2,2,0,0]
    def tight(self,row):
        return sorted(row,key=lambda x:1 if x == 0 else 0)

    # 再依次循环判断两个数是否相等，如果相等，给第一个数乘2，第二个数为0 ==== [2,2,0,0]---->[4,0,0,0]
    def merge(self,row):
        for index in range(3):
            if row[index] == row[index + 1]:
                row[index] *= 2
                row[index + 1] = 0
                # 如果合并完成，分数增加row[index]
                global score
                self.score += row[index]
        return row

    def move_row_left(self,row):
        return self.tight(self.merge(self.tight(row)))

    def move_left(self,field):
        return [self.move_row_left(row) for row in field]


    def move_right(self,field):
        invertField = self.invert(field)
        return self.invert(self.move_left(invertField))


    def move_up(self,field):
        transposeField = self.transpose(field)
        return self.transpose(self.move_left(transposeField))


    def move_down(self,field):
        transposeField = self.transpose(field)
        return self.transpose(self.move_right(transposeField))

    def move(self,direction):

        if direction in self.ismove:
            # 1). 判断这个方向是否可以移动
            if self.ismove[direction](self.field):
                # 2). 执行移动的操作
                self.field = self.moves[direction](self.field)
                # 3). 再随机生成一个2或4
                self.random_create()
            else:
                return False


def get_user_action(stdstr):
    # 获取用户键盘输入的内容
    action = stdstr.getch()
    if action == curses.KEY_UP:
        return 'Up'

    if action == curses.KEY_DOWN:
        return 'Down'

    if action == curses.KEY_LEFT:
        return 'Left'

    if action == curses.KEY_RIGHT:
        return 'Right'

    if action == ord('r'):
        return 'Restart'

    if action == ord('q'):
        return 'Exit'

def main(stdstr):
    game_field = GameField()

    def init():
        game_field.reset()
        game_field.draw(stdstr)
        return 'Game'

    def game():
        # 重新绘制棋盘
        game_field.draw(stdstr)
        action = get_user_action(stdstr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
            return  'Game'

        return 'Game'


    def not_game():
        action = get_user_action(stdstr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'

    state = 'Init'

    state_dict = {
        'Init': init,
        'Game': game,
        'Win': not_game,
        'Gameover': not_game,
        'Exit': exit
    }

    while True:
        state = state_dict[state]()
    #
    # while True:
    #     state = 'Init'
    #     if state == 'Init':
    #         # 初始化游戏
    #         init()
    #     if state == 'Game':
    #         # 进行游戏时，有三种状态----继续游戏(Up,Down,Left,Right)、重新开始(R)、退出游戏(Q)
    #         game()
    #     if state == 'Win':
    #         # 没有进行游戏时，只有两种状态----重新开始(R)、退出游戏(Q)
    #         not_game()
    #     if state == 'Gameover':
    #         not_game()
    #     if state == 'Exit':
    #         # 退出游戏
    #         exit()


curses.wrapper(main)