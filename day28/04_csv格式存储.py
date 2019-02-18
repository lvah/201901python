"""
文件名: $NAME.py
日期: 18  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

csv格式存储： csv文件格式是一种通用的电子表格和数据库导入导出格式。
1:西安邮电:西安:90
1,西安邮电,西安,90


    # 读取csv文件
    import csv
    with open('some.csv', 'rb') as f:        # 采用b的方式处理可以省去很多问题
        reader = csv.reader(f)
        for row in reader:
            # do something with row, such as row[0],row[1]


    import csv
    with open('some.csv', 'wb') as f:      # 采用b的方式处理可以省去很多问题
        writer = csv.writer(f)
        writer.writerows(someiterable)


"""

import csv

with open('doc/example.csv', 'w') as f:
    writer = csv.writer(f)
    # 将列表的每条数据依次写入csv文件， 并以逗号分隔
    writer.writerows([['1', '2', '3'], ['4', '5', '6']])

with open('doc/example.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
