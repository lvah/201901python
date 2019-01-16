"""
文件名: .py
创建时间: 2019-01-16 10:
作者: lvah
联系方式: 976131979@qq.com
代码描述:




1. 1).获取doc里面的文件201901python学员博客整理情况.xlsx, 将作业评分为A的所有学员名称和连接获取;
   2). 将获取的信息保存至Excel表格或者文件中;



2.每一行代表一次单独的销售。列分别是销售产品的类型(A)、产品每磅的价格
(B)、销售的磅数(C),以及这次销售的总收入。TOTAL 列设置为 Excel 公式,将每磅的成本乘以销售的磅数,
并将结果取整到分。有了这个公式,如果列 B 或 C 发生变化,TOTAL 列中的单元格将自动更新.

需要更新的价格如下:
Celery	1.19
Garlic	3.07
Lemon	1.27

现在假设 Garlic、 Celery 和 Lemons 的价格输入的不正确。这让你面对一项无聊
的任务:遍历这个电子表格中的几千行,更新所有 garlic、celery 和 lemon 行中每磅
的价格。你不能简单地对价格查找替换,因为可能有其他的产品价格一样,你不希
望错误地“更正”。对于几千行数据,手工操作可能要几小时。

下载文件: produceSales.xlsx



3. 百度提供的获取天气的api url : http://api.map.baidu.com/telematics/v3/weather?location=%20xian%20&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?%27
    获取当前日期， 及当日温馨提示， 和未来几天的温度；
    并通过微信发送给制定好友.

"""