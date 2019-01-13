"""
文件名: .py
创建时间: 2019-01-05 10:
作者: lvah
联系方式: 976131979@qq.com
代码描述:
# 1. 被人可以正常使用的模块， 你们使用不了；
# 2. 可能会用python的不同版本去写项目；
# 3. 项目里面用的python3.6 --------- itchat
#           - itchat3.10
#           - itchat4.0


# 为什么使用Anaconda？

Python易用,但用好却不易,其中比较头疼的就是包管理和Python不同版本的问题,特别是当你使用Windows的时候。为了解决这些问题,有不少发行版的Python,比如WinPython、Anaconda等,这些发行版将python和许多常用的package打包,方便pythoners直接使用,此外,还有virtualenv、pyenv等工具管理虚拟环境。



常见的问题:
- python解释器中相关模块使用有问题;
- 一台电脑需要编写多个项目， 每个项目的python解释器版本都不同;
- 多个项目中， python解释器版本相同， 但是安装的模块(eg:itchat)的版本不同等问题;




# 什么是Anaconda?

Anaconda是一个用于科学计算的Python发行版,支持 Linux, Mac, Windows系统,提供了包管理与环境管理的功能,可以很方便地解决多版本python并存、切换以及各种第三方包安装问题。Anaconda利用工具/命令 conda 来进行package和environment的管理,并且已经包含了Python和相关的配套工具。




## Anaconda和conda?
- conda 可以理解为一个工具,也是一个可执行命令,其核心功能是包管理与环境管理。
	- 包管理与pip的使用类似;
	- 环境管理则允许用户方便地安装不同版本的python并可以快速切换。

- Anaconda则是一个打包的集合,里面预装好了conda、某个版本的python、众多packages、科学计算工具等等,所以也称为Python的一种发行版。



# 如何使用?
- 1). 创建一个虚拟环境， python版本为3.6， 项目，名为2048；
conda create --name 2048 python==3.6


- 2). 进入虚拟环境
anaconda3：   conda activate  虚拟环境名称
anaconda2：    source activate  虚拟环境名称


- 3). 退出虚拟环境
ctrl+D



- 4). anaconda安装好的虚拟环境存储在哪里?
~/anaconda2/envs/


- 5). 制定虚拟机环境的python解释器位置?
~/anaconda2/envs/虚拟环境名称/bin/python



- 6).

conda install 包名 [-n 虚拟环境名称]
conda search 包名 [-n 虚拟环境名称]
conda remove 包名 [-n 虚拟环境名称]
conda update 包名 [-n 虚拟环境名称]
conda list

7). # 安装pymysql
# 如何配置国内镜像源?

"""