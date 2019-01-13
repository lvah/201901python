"""
日志是用来记录程序在运行过程中发生的状况，在程序开发过程中添加日志模块能够帮助我们了解程序运行过程中发生了哪些事件，这些事件也有轻重之分。
根据事件的轻重可分为以下几个级别：

	DEBUG： 详细信息，通常仅在诊断问题时才受到关注。整数level=10
	INFO： 确认程序按预期工作。整数level=20
	WARNING：出现了异常，但是不影响正常工作.整数level=30
	ERROR：由于某些原因，程序 不能执行某些功能。整数level=40
	CRITICAL：严重的错误，导致程序不能运行。整数level=50

默认的级别是WARNING,也就意味着只有级别大于等于的才会被看到，跟踪日志的方式可以是写入到文件中，也可以直接输出到控制台。


"""
import logging
# 配置日志的信息:
#   1). 日志级别: debug, info, warning, error, critical
#   2). level: 指日志级别为info及以上的日志信息会被记录到文件中;
#   3). format： 指定日志的格式， 可以去logging.Formatter查看参考信息
logging.basicConfig(filename='my.log', level=logging.WARN, format="%(asctime)s-%(filename)s-%(lineno)d- %(levelname)s: %(message)s ")
logging.debug("这是一个调试信息")
logging.error("数据库更新失败")
logging.critical("数据信息删除失败")
