# 1.[Flask整合pyecharts的第一种方式](http://pyecharts.org/#/zh-cn/flask)


# 2.Flask整合Echarts库的第2种方式

Flask 是python web开发的微框架，Echarts酷炫的功能主要是javascript起作用，将两者结合起来，发挥的作用更大。


## 2-1. 静态请求实现步骤


- 1).去官网下载Echarts，如下图所示，下载完整版
- 2). 引入[看Echarts官网文档的教程](https://echarts.baidu.com/tutorial.html#5%20%E5%88%86%E9%92%9F%E4%B8%8A%E6%89%8s)




## 2-2. 动态请求步骤: 使用json和ajax请求

- 什么是ajax?
AJAX = Asynchronous 
JavaScript and XML（异步的 JavaScript 和 XML）。

AJAX 是一种用于创建快速动态网页的技术。通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。
*****这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。*****

- 什么是json?
JSON：JavaScript 对象表示法（JavaScript Object Notation）。JSON 是存储和交换文本信息的语法。类似 XML。



```
@app.route('/getdata')
def get_data():
    language = ['python', 'java', 'c', 'c++', 'c#', 'php']
    value = ['100', '150', '100', '90', '80', '90']
    return json.dumps({'language':language,'value':value},ensure_ascii=False) 
    #如果有中文的话，就需要ensure_ascii=False



# 编写在scripts标签里面，$(function() {});是$(document).ready(function(){ })的简写 
 $(function () {
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById('main'));
            $.ajax({
                url:'/getdata',
                success:function (data) {
                    # 相当于python里面的将json格式解析为字典；
                    json_data=JSON.parse(data)

                    console.info(json_data['language'])
                    console.info(json_data['value'])

                    // 指定图表的配置项和数据
                    var option = {
                        title: {
                            text: '学习语言人数统计'
                        },
                        tooltip: {},
                        legend: {
                            data:['销量']
                        },
                        xAxis: {
                            data: json_data['language']
                        },
                        yAxis: {},
                        series: [{
                            name: '销量',
                            type: 'bar',
                            data: json_data['value']
                        }]
                    };
                    // 使用刚指定的配置项和数据显示图表。
                    myChart.setOption(option);

                }
            })
        })

```