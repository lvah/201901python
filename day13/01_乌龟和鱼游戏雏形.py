"""
# pygame
游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏
    假设游戏场景为范围（x,y）为0<=x<=10,0<=y<=10
    游戏生成1只乌龟和10条鱼
    它们的移动方向均随机
    乌龟的最大移动能力为2（它可以随机选择1还是2移动），鱼儿的最大移动能力是1
    当移动到场景边缘，自动向反方向移动
    乌龟初始化体力为100（上限）
    乌龟每移动一次，体力消耗1
    当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
    鱼暂不计算体力
    当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
"""
import random
class Turtle(object):
    # 构造函数什么时候执行? =---=====创建对象时执行
    def __init__(self):  # self指的是实例化的对象；
        # 乌龟的属性: x,y轴坐标和体力值
        # 乌龟的x轴， 范围1，10

        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)
        # 乌龟初始化体力为100
        self.power = 100

    # 类的方法:
    def move(self):
        # 乌龟的最大移动能力为2,[-2, -1, 0, 1, 2]
        move_skill = [-2, -1, 0, 1, 2]
        # 计算出乌龟的新坐标(10, 12)
        new_x = self.x + random.choice(move_skill)
        new_y = self.y + random.choice(move_skill)

        # 对于新坐标进行检验， 是哦否合法， 如果不合法， 进行处理
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

        # 乌龟每移动一次，体力消耗1
        self.power -= 1

    def is_vaild(self, value):
        """
        判断传进来的x轴坐标或者y轴坐标是否合法?

        1). 如果合法， 直接返回传进来的值；
        2). value<=0;  =====> abs(value);
        3). value > 10 ======> 10-(value-10);

        :param value:
        :return:
        """
        if 1 <= value <= 10:
            return value
        elif value < 1:
            return abs(value)
        else:
            return 10 - (value - 10)

    def eat(self):
        """
        当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
        :return:
        """
        self.power += 20


class Fish(object):
    # 构造函数什么时候执行? =---=====创建对象时执行
    def __init__(self):
        # 鱼的属性: x, y轴坐标
        # 鱼的x轴， 范围1，10
        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    # 类的方法:
    def move(self):
        # 鱼的最大移动能力为1,[ -1, 0, 1]
        move_skill = [-1, 0, 1]
        # 计算出鱼的新坐标(10, 12)
        new_x = self.x + random.choice(move_skill)
        new_y = self.y + random.choice(move_skill)

        # 对于新坐标进行检验， 是否合法， 如果不合法， 进行处理
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

    def is_vaild(self, value):
        """
        判断传进来的x轴坐标或者y轴坐标是否合法?

        1). 如果合法， 直接返回传进来的值；
        2). value<=0;  =====> abs(value);
        3). value > 10 ======> 10-(value-10);

        :param value:
        :return:
        """
        if 1 <= value <= 10:
            return value
        elif value < 1:
            return abs(value)
        else:
            return 10 - (value - 10)


def main():
    # 创建一个乌龟;
    turtle = Turtle()
    print(turtle.x, turtle.y)

    # for循环创建10个鱼
    # fishs = []
    # for i in range(10):
    #     fishs.append(Fish())

    # 创建10个鱼对象;
    fishs = [Fish() for i in range(10)]

    # 游戏开始
    while True:
        # 判断游戏是否结束?( 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束)
        if turtle.power <= 0:
            print("乌龟没有体力了， Game over......")
            break
        elif len(fishs) == 0:
            print("鱼被吃光， Game over......")
            break
        else:
            # 游戏没有结束. 乌龟和鱼随机移动
            turtle.move()
            # 鱼移动
            for fish in fishs:
                fish.move()
                # 判断鱼是否被乌龟吃掉？
                # 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
                if turtle.x == fish.x and turtle.y == fish.y:
                    turtle.eat()
                    # 删除被乌龟吃掉的鱼
                    fishs.remove(fish)
                    print("鱼被乌龟吃掉， 还剩%d条鱼....." % (len(fishs)))
                    print("乌龟的最新体力为%s" % (turtle.power))

            # 乌龟跟10个鱼都比较结束后， 没有发现吃到一个鱼， 才执行， 跟for是一块的；
            else:
                print("乌龟没有吃到鱼，最新体力为%s" % (turtle.power))


# pygame
if __name__ == "__main__":
    print("游戏开始".center(30, "*"))
    main()
