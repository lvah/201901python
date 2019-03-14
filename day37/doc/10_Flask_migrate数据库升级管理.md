# 1.  什么是Flask-Migrate?
    Flask-Migrate是一个为Flask应用处理SQLAlchemy数据库迁移的扩展，使得可以通过Flask的命令行接口或者Flask-Scripts对数据库进行操作。


# 2. 如何安装Flask-Migrate?

```
pip install flask-migrate
```


# 3. 如何配置?

```
app = Flask(__name__)

app.config.from_envvar('config.py')
db = SQLAlchemy(app) 

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

```




# 4. 如何使用?

- 1). 创建迁移仓库(migrations目录)

python script.py  db init

- 2). 读取类的内容, 生成版本文件,  并没有真正在数据库中添加或删除;

python  script.py  db migrate -m "版本名后缀"

- 3). 在数据库中增删改, 也就是将迁移应用于数据库;

    python script.py  db upgrade

- 4). 检测是否成功?

mysql -uroot -pwestos

- 5). 去查看改变的历史状态;

python script.py  db history

- 6). 返回指定的版本状态;降级数据库,不指定版本则是最老版本

python script.py  db downgrade  base

- 7). 显示当前版本

python data_migrate.py db current 

- 8). 升级版本,不指定版本为最新版本

python data_migrate.py db upgrade 版本号

- 7). 帮助，查找所有命令

python data_migrate.py db --help 

