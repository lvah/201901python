"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




案例:
    假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)
    三天的票房,为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据?

    a = ["猩球崛起3：终极之战”,"敦刻尔克”,"蜘蛛侠：英雄归来”,"战狼2”]
    b_16 = [15746,312,4497,319]
    b_15 = [12357,156,2045,168]
    b_14 = [2358,399,2358,362]

    数据来源: http://www.cbooo.cn/movieday

"""

from matplotlib import pyplot as plt
from matplotlib import font_manager

#  中文显示乱码问题;
myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=24)

x_movies_name = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
y_16 = [15746, 312, 4497, 319]
y_15 = [12357, 156, 2045, 168]
y_14 = [2358, 399, 2358, 362]

#   如何设置图片的大小；
plt.figure(figsize=(30, 10))

# 生成竖向的条形图
bar_width = 0.3

x_range = range(len(x_movies_name))
# ['a', 'b', 'c', 'd'] ===== [0, 1,2,3]
# [1,2,3,4]
# [3,4,4,4]

# [(0, 1), (1, 2), (2, 3), (3, 4)]
# [(0+0.3, 1), (1+0.3, 3)]
plt.bar(x_range, y_14, color='green', width=bar_width, label="2017-09-14票房数据")
plt.bar([i + bar_width for i in x_range], y_15, color='red', width=bar_width, label="2017-09-15票房数据")
plt.bar([i + bar_width * 2 for i in x_range], y_16, color='orange', width=bar_width, label="2017-09-16票房数据")
# 修改刻度信息的配置
plt.xticks(range(len(x_movies_name)), labels=x_movies_name, fontproperties=myfont, rotation=45)

# 3). x轴和y轴的描述信息；
plt.title("某年内地电影票房前20的电影和电影票房数据", fontproperties=titlefont)
plt.xlabel("电影名", fontproperties=myfont)
plt.ylabel("电影票房(单位:亿)", fontproperties=myfont)
plt.savefig('doc/bar.png')
