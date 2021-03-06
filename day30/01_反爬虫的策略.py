"""
文件名: $NAME.py
日期: 21  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

                                scrapy反爬


# 策略一：设置download_delay

        - 作用:设置下载的等待时间，大规模集中的访问对服务器的影响最大，相当与短时间中增大服务器负载。

        - 缺点: 下载等待时间长，不能满足段时间大规模抓取的要求，太短则大大增加了被ban的几率



# 策略二：禁止cookies
        - Cookie，有时也用其复数形式 Cookies，指某些网站为了辨别用户身份、进行 session
        跟踪而储存在用户本地终端上的数据（通常经过加密）。
        - 作用: 禁止cookies也就防止了可能使用cookies识别爬虫轨迹的网站得逞。
        - 实现: COOKIES_ENABLES=False


# 策略三：使用user agent池(拓展: 用户代理中间件)
        - 为什么使用? scrapy本身是使用Scrapy/0.22.2来表明自己身份的。这也就暴露了自己是爬虫的信息。
        - user agent，是指包含浏览器信息、操作系统信息等的一个字符串，也称之为一种特殊的网络协议。服务
        器通过它判断当前访问对象是浏览器、邮件客户端还是网络爬虫。
****补充。。。。


# 策略四：使用代理IP中间件
web server应对爬虫的策略之一就是直接将你的IP或者是整个IP段都封掉禁止访问，
这时候，当IP封掉后，转换到其他的IP继续访问即可。


****补充。。。。
# 策略五: 分布式爬虫Scrapy+Redis+MySQL   # 多进程
     Scrapy-Redis则是一个基于Redis的Scrapy分布式组件。
     它利用Redis对用于爬取的请求(Requests)进行存储和调度(Schedule)，
     并对爬取产生rapy一些比较关键的代码，将scrapy变成一个可以在多个主
     机上同时运行的分布式爬虫。



"""