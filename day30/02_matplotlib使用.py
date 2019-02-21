"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

- Matplotlib
    - matplotlib是什么?
    - matplotlib的基本要点
    - matplotlib的折线图， 柱状图， 直方图， 散点图;
    - 更多的画图工具


# 1. matplotlib是什么? python底层的绘图工具


# 2. matplotlib的基本要点：
- 如何设置图片的大小；
- 如何保存到本地；
- x轴和y轴的描述信息；
- 中文显示乱码问题;
- 调整x轴和y轴的刻度;
- x轴的刻度信息过长， 如何调整？
- 标记最高点;


"""

# 案例1: 假设一天中每隔两个小时气温变化的折线图绘制;
from matplotlib import pyplot as plt
from matplotlib import font_manager
# 4). 中文显示乱码问题;
myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=24)
# 图表的x轴的数据, 是一个可迭代的数据类型
x_times = range(0, 24, 2)
# 图表的y轴的数据, 是一个可迭代的数据类型
y_temp = [15, 12, 13, 20, 23, 30, 15, 12, 13, 20, 23, 30]

# min(y_temp), max(y_temp)

#  1). 如何设置图片的大小；
plt.figure(figsize=(10, 10))

# 传入x和y轴的数据， 绘制图形;
plt.plot(x_times, y_temp)

# 3). x轴和y轴的描述信息；
plt.title("每天的气温变化(每隔两个小时)",fontproperties=titlefont )
plt.xlabel("时间", fontproperties=myfont)
plt.ylabel("温度", fontproperties=myfont)

# 5). 调整x轴和y轴的刻度;
# 6). x轴的刻度信息过长， 如何调整？
plt.xticks(x_times, labels=["%s时0分"%(i) for i in x_times], fontproperties=myfont, rotation=45)
y_temp_range = range(min(y_temp), max(y_temp)+1, 2)
plt.yticks(y_temp_range, labels=["%s 。C"%(i) for i in y_temp_range], fontproperties=myfont)

#
plt.scatter(x_times[2], y_temp[2], color='b')
plt.scatter(x_times[2], y_temp[2], color='', marker='o', edgecolors='r', s=300)

# 2). 如何保存到本地；
plt.savefig('doc/temp.png')

# 在执行程序时显示图像
# plt.show()
