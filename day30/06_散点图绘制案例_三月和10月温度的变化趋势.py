"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

1. 需求：
        绘制北京3,10月份每天白天的最高气温随时间(天)变化的散点图，并找出规律
        数据来源：天气网  http://lishi.tianqi.com/beijing/index.html
        a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
        b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
难点：
        散点图语法
        绘制两边分布式x轴坐标


目前难点: 10月的x轴坐标变化



"""

from matplotlib import pyplot as plt
from matplotlib import font_manager

#  中文显示乱码问题;
myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=24)

# 图表的x轴的数据, 是一个可迭代的数据类型
x_march = range(1, 32)
x_oct = range(50, 81)

# 图表的y轴的数据, 是一个可迭代的数据类型
y_temp_march = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21,
                22, 22, 22, 23]
y_temp_oct = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11,
              13, 12, 13, 6]

#   如何设置图片的大小；
plt.figure(figsize=(30, 10))

# 传入x和y轴的数据， 绘制图形;
plt.scatter(x_march, y_temp_march, label="3月的温度变化", color='r', alpha=0.5)
plt.scatter(x_oct, y_temp_oct, label="10月的温度变化", color='g', alpha=0.5)

# 3). x轴和y轴的描述信息；
plt.title("北京3,10月份每天白天的最高气温随时间(天)变化的散点图", fontproperties=titlefont)
plt.xlabel("时间", fontproperties=myfont)
plt.ylabel("温度", fontproperties=myfont)

# 5). 调整x轴和y轴的刻度;
# 6). x轴的刻度信息过长， 如何调整？
_x_info = list(x_march) + list(x_oct)
_x_labels_march = ["3月%s日" % (i) for i in x_march]
_x_labels_oct = ["10月%s日" % (i - 49) for i in x_oct]  # range(50, 81)
plt.xticks(_x_info[::3], labels=(_x_labels_march + _x_labels_oct)[::3], fontproperties=myfont, rotation=45)

plt.legend(prop=myfont, loc="upper left")
plt.grid(alpha=0.5)

# 2). 如何保存到本地；
plt.savefig('doc/scatter.png')

# 在执行程序时显示图像
# plt.show()
