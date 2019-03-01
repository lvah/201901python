"""
文件名: $NAME.py
日期: 28  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 




# 1. 如何实现闪现?
    1). flash消息这种功能，是Flask的核心特性。用于在下一个响应中显示一个消息，让用户知道状态发生了变化。
    可以使确认消息，警告或者错误提醒。

    flash("闪现的消息")


    2). 工作原理:
        闪现系统使得在一个请求结束的时候记录一个信息，然后在且仅仅在下一个请求中访问这个数据。

# 2. html代码中如何调用闪现内容?
    仅调用flash()函数并不能把消息显示出来，程序使用的模板要渲染这些消息。
    Flask把get_flashed_messages()函数开放给模板，用来获取并渲染消息


{#让每个页面都可以获取闪现信息闪现#}
{% for item in get_flashed_messages() %}

    <div class="alert alert-warning alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                aria-hidden="true">&times;</span></button>
        {{ item }}
    </div>
{% endfor %}


"""





