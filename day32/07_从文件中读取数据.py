"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



# csv, excel, json........
# 1). csv文件的写入

df = pd.DataFrame(
    {'province': ['陕西', '陕西', '四川', '四川', '陕西'],
     'city': ['咸阳', '宝鸡', '成都', '成都', '宝鸡'],
     'count1': [1, 2, 3, 4, 5],
     'count2': [1, 2, 33, 4, 5]
     }
)

df.to_csv('doc/csvFile.csv')
print("csv文件保存成功")

# 2). csv文件的读取
df2 = pd.read_csv('doc/csvFile.csv')
print(df2)

# 3). excel文件的写入
df2.to_excel("/tmp/excelFile.xlsx", sheet_name="省份统计")
print("excel文件保存成功")





# 练习:
#  文件的描述信息: 订单编号, 订单数量, 商品名称， 商品详细选择项， 商品价格
# 1). 从文件中读取所有的数据;
# 2). 获取数据中所有的商品名称；
# 3）. 跟据商品的价格进行排序， 降序，
# 将价格最高的20件产品信息写入mosthighPrice.xlsx文件中;