"""
文件名: write_sql.py
创建时间: 2019-03-29 12:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""



import pandas


df  = pandas.read_csv('movie.csv', names=['name', 'logo', 'actors', 'release_time', 'detail_url', 'tag', 'area', 'length', 'info'])
print(df.describe())
print(df['tag'].unique())




