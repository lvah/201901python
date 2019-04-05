# 1. 安装python数据库连接依赖包
```
pip install flask-sqlalchemy

```

- [flask-sqlalchemy中文文档](http://www.pythondoc.com/flask-sqlalchemy/index.html)
- [查看配置键](http://www.pythondoc.com/flask-sqlalchemy/config.html#id2)




# 2. 重要的连接配置


- 用于连接数据库的URI: SQLALCHEMY_DATABASE_URI

        - mysql: mysql://username:password@server/db
        - sqlite: sqlite:///tmp/xxx.db

- 用来追踪数据库对象的配置:SQLALCHEMY_TRACK_MODIFICATIONS


# 3. 安装数据库(自行整理)


# 4. 创建数据库
 create database MovieProject  default charset utf8;
