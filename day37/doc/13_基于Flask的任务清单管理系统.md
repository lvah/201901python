##  1.目标

本项目将学习 Mariadb 作为数据库后端，Bootstrap 作为前端的技术栈，并实现一个清单应用。从中我们可以学习 Flask Web 应用框架，及 Mariadb 关系型数据库和 BootStrap web开发框架。




## 2.项目介绍

本应用修改自 TodoMVC 的 todo list 应用，使用 Mariadb 作为数据库后端，Bootstrap 作为前端的 Flask 应用。先给它起个好听的名字吧，方便之后称呼。

todo list => (自定义，随便起名称)  => todoest


就像一般的 todo list 应用一样，todoest 实现了以下功能：
- 管理数据库连接
- 列出所有的 todo 项
- 创建新的 todo
- 检索单个 todo
- 编辑单个 todo 或将其标记为已完成
- 删除单个 todo




## 3.项目效果



- 新建标签页，启动 todoest


- 打开浏览器访问 http://localhost:8000/



## 4.技术分析


- 为什么选择Flask?

	Flask是一个使用 Python 编写的轻量级 Web 应用框架。其 WSGI 工具箱采用 Werkzeug ，模板引擎则使用 Jinja2 。Flask使用 BSD 授权。
    Flask也被称为 “microframework” ，因为它使用简单的核心，用 extension 增加其他功能。Flask没有默认使用的数据库、窗体验证工具。
    因此Flask是一个使用Python编写的轻量级Web应用框架。轻巧易扩展，而且够主流，有问题不怕找不到人问，最适合 todoest 这种轻应用了。


- 为什么选择Mariadb?

    MariaDB数据库管理系统是MySQL的一个分支，主要由开源社区在维护，采用GPL授权许可 MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品。MariaDB虽然被视为MySQL数据库的替代品，但它在扩展功能、存储引擎以及一些新的功能改进方面都强过MySQL。而且从MySQL迁移到MariaDB也是非常简单的.


-  为什么选择Bootstrap?

    Bootstrap是美国Twitter公司的设计师Mark Otto和Jacob Thornton合作基于HTML、CSS、JavaScript 开发的简洁、直观、强悍的前端开发框架，使得 Web 开发更加快捷。

    Bootstrap中包含了丰富的Web组件，根据这些组件，可以快速的搭建一个漂亮、功能完备的网站。其中包括以下组件：下拉菜单、按钮组、按钮下拉菜单、导航、导航条、路径导航、分页、排版、缩略图、警告对话框、进度条、媒体对象等