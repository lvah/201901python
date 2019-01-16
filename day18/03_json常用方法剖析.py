"""
文件名: .py
创建时间: 2019-01-16 11:
作者: lvah
联系方式: 976131979@qq.com
代码描述:

使用 JSON 函数需要导入 json 库：import json。

json.dumps      将 Python 对象编码成 JSON 字符串
json.loads      将已编码的 JSON 字符串解码为 Python 对象

json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
            allow_nan=True, cls=None, indent=None,
            separators=None, encoding="utf-8", default=None,
            sort_keys=False, **kw)
# 案例:
print(json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))



"""

import json

# python对象编码成为json的数据格式;
d = {'key%s' % (i): 'value%s' % (i) for i in range(1000)}
jsonStr = json.dumps(d)
print(jsonStr, type(jsonStr))
l = [1, 2, 3, 4]
jsonLi = json.dumps(l)
print(jsonLi, type(jsonLi))

# python对象编码为json格式， 并保存到制定文件中;
with open('doc/test01.json', 'w') as f:
    # indent: 是否设置缩进; sort_keys: 是否对key值进行排序;
    # separators = {"每个元素之间的分隔符", “key和value值之间的分隔符”}
    json.dump(d, f, indent=4, sort_keys=True, separators=(',', ': '))

# json对象解码成为python的数据格式;
pythonDict = json.loads(jsonStr)
print(pythonDict, type(pythonDict))

# json对象(存储在json文件)解码成为python的数据格式;
with open('doc/test01.json') as f:
    pythonObj = json.load(f)
    print(pythonObj, type(pythonObj))
