"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

需求1:
    绘制10点到12点每分钟的气温， 如何绘制折线图观察每分钟气温的变化情况?
    temps = [random.randint(20, 35) for i in range(120)]


    10时10分  10时20分



需求2：假设大家在30岁的时候，根据自己的实际情况统计出来从11岁到30岁每年交的女
（男）朋友的数量如a，请绘制出该数据的折线图，以便分析每年交女（男）朋友的数量走势；


需求3：
    假设大家30岁时统计出你和你同桌各自从11岁到30岁每年交女（男）朋友的数量如列表a和b，
    请在一个图中展示数据折线图，以便比较两人20年之间每年交女（男）朋友的数量走势

"""
import random

from matplotlib import pyplot as plt
from matplotlib import font_manager
# 4). 中文显示乱码问题;
myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=24)
# 图表的x轴的数据, 是一个可迭代的数据类型
x_times = range(0,120)
# 图表的y轴的数据, 是一个可迭代的数据类型
y_temp = [random.randint(20, 35) for i in range(120)]

# min(y_temp), max(y_temp)

#  1). 如何设置图片的大小；
plt.figure(figsize=(20, 20))

# 传入x和y轴的数据， 绘制图形;
plt.plot(x_times, y_temp)

# 3). x轴和y轴的描述信息；
plt.title("10点到11点温度变化)",fontproperties=titlefont )
plt.xlabel("时间", fontproperties=myfont)
plt.ylabel("温度", fontproperties=myfont)

# 5). 调整x轴和y轴的刻度;
# 6). x轴的刻度信息过长， 如何调整？

# 10时10分
# 11时10分
_x_labels = ["10时%s分" %(i) for i in range(0, 60, 10)]
_x_labels += ["11时%s分" %(i) for i in range(0, 60, 10)]
plt.xticks(x_times[::10], labels=_x_labels, fontproperties=myfont, rotation=45)
y_temp_range = range(min(y_temp), max(y_temp)+1, 2)
plt.yticks(y_temp_range, labels=["%s 。C"%(i) for i in y_temp_range], fontproperties=myfont)

# #
# plt.scatter(x_times[2], y_temp[2], color='b')
# plt.scatter(x_times[2], y_temp[2], color='', marker='o', edgecolors='r', s=300)

# 2). 如何保存到本地；
plt.savefig('doc/temp3.png')

# 在执行程序时显示图像
# plt.show()









from matplotlib import pyplot as plt, font_manager

# myfont=font_manager.FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc",size=18)
# titlefont=font_manager.FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc",size=25)
#
#
# x_times=range(0,13,1)
# y_temp=[12,14,15,18,20,2,12,18,15,13,14,2,5]
# def times():
#     h=10
#     li=[]
#     for m in range(0,130,10):
#         if 120>m>=60:
#             h=11
#             m=m-60
#         if m>=120:
#             h=12
#             m=m-120
#         li.append('%s时%s分' %(h,m))
#     return li
#
# plt.title('每十分钟气温变化',fontproperties=titlefont)
#
# plt.figure(figsize=(15,15))
# plt.plot(x_times,y_temp)
# plt.xlabel('时间',fontproperties=myfont)
# plt.xticks(x_times,labels=times(),fontproperties=myfont,rotation=45)
# plt.ylabel('温度',fontproperties=myfont)
# plt.savefig('doc/temp2.png')
