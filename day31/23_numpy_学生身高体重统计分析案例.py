"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


需求1:
    获取所有男生的身高, 求平均值;获取所有女生的身高, 求平均值;并绘制柱状图显示




import numpy as np
from pyecharts import  Bar
fname = "doc/eg6-a-student-data.txt"
dtype = np.dtype([('gender', '|S1'), ('height', 'f2')])
data = np.loadtxt(fname=fname, dtype=dtype, skiprows=9,
                  usecols=(1, 3))
# print(data)
# print(data['gender'])
# print(data['height'])
# print(data['height'][data['gender'] == b'M'].mean())
# print(data['height'][data['gender'] == b'F'].mean())
#


# 判断是否性别为那男的表达式
isMale = data['gender'] == b'M'
male_avg_height = data['height'][isMale].mean()
female_avg_height = data['height'][~isMale].mean()
print(male_avg_height, female_avg_height)

bar = Bar(title="不同性别身高的平均值")
bar.add("", ["男", '女'], [male_avg_height, female_avg_height])
bar.render()



需求2:
    获取所有男生的体重, 求平均值;获取所有女生的体重, 求平均值;并绘制柱状图显示

    def parser_weight(weight):
    # 对于体重数据的处理, 如果不能转换为浮点数据类型, 则返回缺失值;
    try:
        return  float(weight)
    except ValueError as e:
        return  -99

fname = "doc/eg6-a-student-data.txt"
dtype = np.dtype([('gender', '|S1'), ('height', 'f2'), ('weight', 'f2')])
data = np.loadtxt(fname=fname, dtype=dtype, skiprows=9,
                  usecols=(1, 3, 4), converters={4:parser_weight})

# 判断是否性别为男的平均身高
isMale = data['gender'] == b'M'
male_avg_height = data['height'][isMale].mean()
female_avg_height = data['height'][~isMale].mean()
print(male_avg_height, female_avg_height)



# 判断是否性别为男的平均体重
is_weight_vaild =  data['weight'] > 0
male_avg_weight = data['weight'][isMale & is_weight_vaild].mean()
female_avg_weight = data['weight'][~isMale & is_weight_vaild].mean()
print(male_avg_weight, female_avg_weight)


bar = Bar(title="不同性别身高的平均值")
bar.add("身高", ["男", '女'], [male_avg_height, female_avg_height])
bar.add("体重", ["男", '女'], [male_avg_weight, female_avg_weight])
bar.render()



"""


import numpy as np
from pyecharts import  Bar

#
# def parser_bps(bps):
#     # 对于体重数据的处理, 如果不能转换为浮点数据类型, 则返回缺失值;
#     try:
#
#         bps = bps.decode('utf-8').split('/')
#         print(bps, type(bps))
#         first_bps = float(bps[0])
#         second_bps = float(bps[1])
#         return first_bps, second_bps
#     except ValueError as e:
#         return -99


def parser_bpd(bpd):
    # 对于体重数据的处理, 如果不能转换为浮点数据类型, 则返回缺失值;
    try:
        return float(bpd)
    except ValueError as e:
        return -99

fname = "doc/eg6-a-student-data.txt"
dtype = np.dtype([('gender', '|S1'),  ('bpd', 'f2')])
data = np.loadtxt(fname=fname, dtype=dtype, skiprows=9,
                  usecols=(1,  6), converters={ 6:parser_bpd})

print(data)

