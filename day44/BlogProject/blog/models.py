from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# 1). 博客需要记录什么?(头脑风暴)
# 博客标题， 博客最后一次修改的时间， 博客的阅读数， 博客的评论数， 博客的内容， 博客的创建者名称， 标签， 分类
# 2). 设计博客的数据库模型
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="分类名", db_index=True)

    class Meta():
        db_table = "分类名"
        ordering = ['id']

    def __str__(self):
        return  self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name="标签名", db_index=True)

    class Meta():
        db_table = "标签名"


    def __str__(self):
        return  self.name


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    body = models.TextField()  # 博客内容

    # 创建博客的时间
    created_time = models.DateTimeField()
    # 最后依次修改博客的时间
    modified_time = models.DateTimeField()
    # 阅读量
    read_num = models.IntegerField(default=0)
    # 评论数量
    comment_num = models.IntegerField(default=0)

    # 标签-博客(多对多)，
    tags = models.ManyToManyField(Tag)
    # 分类-分类(一对多)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # 博客的创建者名称, 必须是系统存在的用户;
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return  self.title