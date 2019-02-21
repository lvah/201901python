"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



需求2：假设大家在30岁的时候，根据自己的实际情况统计出来从11岁到30岁每年交的女
（男）朋友的数量如a，请绘制出该数据的折线图，以便分析每年交女（男）朋友的数量走势；



"""
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

x_age = range(11, 31)
y_count = [random.randint(0, 5) for i in range(20)]
myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=14)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=20)

plt.figure(figsize=(10, 10))
plt.plot(x_age, y_count)
plt.title("11岁至30岁所交男(女)友个数", fontproperties=titlefont)
plt.xlabel("年龄", fontproperties=myfont)
plt.ylabel("女(男)友数量", fontproperties=myfont)


plt.xticks(x_age, labels=["%s岁" %(item) for item in x_age], fontproperties=myfont, rotation=45)
plt.scatter(x_age[0], y_count[0], c='r')

plt.savefig('doc/age.png')
