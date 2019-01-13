import curses
from itertools import chain
from random import choice

import time


class GameField(object):
    # 初始化信息
    def __init__(self, width=4, height=4, win_value=2048):
        self.width = width
        self.height = height
        self.win_value = win_value
        self.score = 0  # 当前得分
        self.highscore = 0  # 最高分
        self.moves = {}
        self.moves['Left'] = self.is_move_left
        self.moves['Right'] = self.is_move_right
        self.moves['Down'] = self.is_move_down
        self.moves['Up'] = self.is_move_up

        self.movesDict = {}
        self.movesDict['Left'] = self.move_left
        self.movesDict['Right'] = self.move_right
        self.movesDict['Down'] = self.move_down
        self.movesDict['Up'] = self.move_up

    def reset(self):  # 重置棋盘
        if self.score > self.highscore:
            self.highscore = self.score  # 更新最高分
        self.score = 0
        # 需求1: 生成4*4的棋盘， 其中数据结构选择列表嵌套列表;
        self.field = [[0 for j in range(self.width)]
                      for i in range(self.height)]

        # 在棋盘的一个随机位置插入一个数字2或者4
        self.random_create()
        self.random_create()

    def random_create(self):
        # 在棋盘的一个随机位置插入一个数字2或者4
        # field[0][3] = 2
        while True:
            i, j = choice(range(self.height)), choice(range(self.width))
            if self.field[i][j] == 0:
                self.field[i][j] = choice([2, 2, 2, 4])
                break

    def draw(self, stdscr):
        def draw_sep():
            stdscr.addstr('+' + "----+" * self.width + '\n')

        def draw_one_row(row):
            stdscr.addstr("".join('|{:^4}'.format(num) if num != 0 else "|    " for num in row) + '|' + '\n')

        # 清屏
        stdscr.clear()
        stdscr.addstr("2048".center(50, '-') + '\n')
        stdscr.addstr("当前分数:" + str(self.score) + '\n')
        if self.highscore != 0:
            stdscr.addstr("最高分:" + str(self.highscore) + '\n')
        for row in self.field:
            draw_sep()
            draw_one_row(row)
        draw_sep()

        # 判断是否赢或者输
        if self.is_win():
            stdscr.addstr("胜利!!!!" + '\n')
        if self.is_gameover():
            stdscr.addstr("游戏结束!!!!" + '\n')
        stdscr.addstr(" 游戏帮助: 上下左右键  (R)Restart     Q(Quit)")

    def is_win(self):
        return max(chain(*self.field)) >= self.win_value

    def is_gameover(self):
        # 任何方向都不能移动的时候， 游戏结束
        return not any([self.move_is_possible(direction)
                        for direction in self.moves])

    @staticmethod
    def invert(field):
        # 矩阵进行反转
        return [row[::-1] for row in field]
        # print(invert(li))

    @staticmethod
    # 矩阵的转置
    def transpose(field):
        # *field ==== [1,2,3] [4,5,6] [7,8,9]
        # zip(*field)   =====  [1,4,7], [2,5,8] [3,6,9]
        # list(zip(*field)) ======  [(1, 4, 7), (2, 5, 8), (3, 6, 9)]  但是将来元素需要修改，必须转换为列表
        return [list(row) for row in zip(*field)]

    @staticmethod
    def is_row_change(row):
        # row
        # 需求3. 判断一行内容是否可移动。
        def is_change(i):  # 0
            # 判断每两个元素之间是否可移动
            if row[i] == 0 and row[i + 1] != 0:
                return True
            if row[i] != 0 and row[i] == row[i + 1]:
                return True
            return False

        return any([is_change(index) for index in range(len(row) - 1)])

    # 判断这个棋盘是否可向左移动
    def is_move_left(self, field):
        return any([self.is_row_change(row) for row in field])

    def is_move_right(self, field):
        #  对于列表元素进行反转
        field = self.invert(field)
        print(field)
        return self.is_move_left(field)

    def is_move_up(self, field):
        # 对于列表元素进行转置
        field = self.transpose(field)
        return self.is_move_left(field)

    def is_move_down(self, field):
        # 反转+ 转置
        field = self.transpose(field)
        return self.is_move_right(field)

    def move_is_possible(self, direction):  # 'left'
        # 判断用户选择的方向是否可移动
        if direction in self.moves:
            return self.moves[direction](self.field)
        else:
            return False

    # 将棋盘每一行的非0数向前移动， 0向后移动;
    @staticmethod
    def tight(row):  # [2, 0, 2, 0]
        # 最快的方式， 通过排序实现...........
        return sorted(row, key=lambda x: 1 if x == 0 else 0)

    def merge(self, row):  # [2,2,0,0]
        # [0,1,2]
        for i in range(len(row) - 1):
            # 如果两个值相等， 前一个元素*2, 后一个元素改为0。
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
                # 如果覆盖成功， 就给得分

                self.score += row[i]
        return row  # [4, 0, 0, 0]

    def move_row_left(self, row):
        return self.tight(self.merge(self.tight(row)))

    def move_left(self, field):
        return [self.move_row_left(row) for row in field]

    def move_right(self, field):
        field = self.invert(field)
        return self.invert([self.move_row_left(row) for row in field])

    def move_up(self, field):
        return self.transpose(self.move_left(self.transpose(field)))

    def move_down(self, field):
        return self.transpose(self.move_right(self.transpose(field)))

    def move(self, direction):  # 'left'
        # 判断用户选择的方向是否可移动

        if direction in self.movesDict:
            # 判断是否可移动
            if self.move_is_possible(direction):
                self.field = self.movesDict[direction](self.field)
                self.random_create()
                return True
        else:
            return False


def get_user_action(stdscr):
    action = stdscr.getch()
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


def main(stdscr):
    action = stdscr.getch()

    def init():
        # 初始化棋盘的操作
        game_field.reset()
        game_field.draw(stdscr)
        return 'Game'

    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'GameOver'
        return 'Game'

    def not_game():
        game_field.draw(stdscr)
        while True:
            action = get_user_action(stdscr)
            if action == 'Restart':
                return 'Init'
            if action == 'Exit':
                return 'Exit'

    state_actions = {
        'Init': init,
        'Game': game,
        'Win': not_game,
        'GameOver': not_game,

    }
    game_field = GameField()
    state = 'Init'

    # 如果当前状态不是退出， 那么一直执行
    while state != 'Exit':
        # 执行当前状态需要操作的内容， 并返回， 下一次的状态为什么.
        state = state_actions[state]()


curses.wrapper(main)