from django.db import models

# Create your models here.
from datetime import date

from django.db import models
from django.utils import timezone




# 上传文件的编写
class MyBook(models.Model):
    name = models.CharField(max_length=100, verbose_name="书籍名称", db_index=True)
    # verbose_name: 后台管理的前端页面字段名的中文显示;
    # upload_to: 上传的指定位置； 这里是相对位置，(settings文件中必须设置MEDIA_ROOT变量的内容;)
    logo = models.ImageField(verbose_name="图书封面", upload_to="modelTest/")
    # blank=True， 字段信息可以为空白;
    pubdate  = models.DateField(db_column="出版日期", verbose_name="出版日期")
    read_num = models.IntegerField(null=True, default=0)

    class Meta():
        # 修改默认的表名为指定的表名(书籍)
        db_table = "书籍"
        # 默认是升序，
        # ordering = ['pubdate']
        # 指定按出版日期的降序进行排序;如果出版日期相同， 则按照阅读量进行降序排；
        ordering = ['-pubdate', '-read_num']


    def __str__(self):
        return  self.name

# 一个用户可以属于多个组； 一个组里面可以有多个用户； ===========多对多关系
# 用户:
# 组:
# 用户表
class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")
    def __str__(self):
        return  self.name
# 用户组 类名: Group  ----> modelTest_group(数据库表存储的表名)
class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="组名")
    # 设置多对多关系，并且必须关联关系表；through
    persons = models.ManyToManyField(Person, through='GrouPersons')
    # person = models.OneToOneField(Person)  # 设置一对一关系

    def __str__(self):
        return  self.name
# 我想记录某个用户加入某个组的时间和原因；
class GrouPersons(models.Model):
    # 级联不删除， 默认设置为空;
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateField(default=timezone.now()) # 某个用户加入某个组的日期;
    join_reason = models.CharField(max_length=200)  # 某个用户加入某个组的原因;

    def __str__(self):
        return  "%s-%s" %(self.group, self.person)



#
# >>> person2 = Person(name="小明")
# >>> person1 = Person(name="张三")
# >>> group1 = Group(name = "Linux兴趣小组")
# >>> group2 = Group(name = "python兴趣小组")
# >>> person1.save()
# >>> person2.save()
# >>> group1.save()
# >>> group2.save()
# >>> r1 = GrouPersons(person=person1, group=group1, join_reason='好玩')
# >>> r1.save()
# >>> group1.persons.all()
# <QuerySet [<Person: 张三>]>
# >>> r2 = GrouPersons(person=person1, group=group2, join_reason='好玩')
# >>> r2.save()
# >>> group2.persons.all()
# <QuerySet [<Person: 张三>]>
# >>> person1.group_set.all()
# <QuerySet [<Group: Linux兴趣小组>, <Group: python兴趣小组>]>



