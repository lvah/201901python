"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


需求3：
    假设大家30岁时统计出你和你同桌各自从11岁到30岁每年交女（男）朋友的数量如列表a和b，
    请在一个图中展示数据折线图，以便比较两人20年之间每年交女（男）朋友的数量走势


"""
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

x_age = range(11, 31)
y_count_1 = [random.randint(0, 5) for i in range(20)]
y_count_2 = [random.randint(0, 5) for j in range(20)]
myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=14)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=20)

plt.figure(figsize=(10, 10))

# 在同一个图里面绘制多条折线,
#  color: 线条颜色
#  linestyle： 线条的风格
#  linewidth: 线条的粗细
#  alpha: 透明度
plt.plot(x_age, y_count_1, color='g', linestyle='-.', linewidth=5, alpha=0.5, label="自己")
plt.plot(x_age, y_count_2, color='r', linestyle='--', linewidth=3, alpha=0.3, label="同桌")

# 添加图例
plt.legend(loc="upper right", prop=titlefont)

# 添加网格
plt.grid(alpha=0.3)

plt.title("11岁至30岁所交男(女)友个数", fontproperties=titlefont)
plt.xlabel("年龄", fontproperties=myfont)
plt.ylabel("女(男)友数量", fontproperties=myfont)


plt.xticks(x_age, labels=["%s岁" %(item) for item in x_age], fontproperties=myfont, rotation=45)
plt.scatter(x_age[0], y_count_1[0], c='r')

plt.savefig('doc/age02.png')
