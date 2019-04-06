from django.db import models

# Create your models here.


# 关于评论的数据库设计
class Comment(models.Model):
    name = models.CharField(max_length=30, verbose_name="评论人")
    email = models.EmailField(max_length=50, verbose_name="邮箱地址")
    # 评论内容
    text  = models.TextField(verbose_name="评论内容")
    # auto_now: 创建对象时， 将当前时间记录到数据库中;
    # auto_now_add: 更新对象时， 会更新这个时间为当前时间;
    created_time = models.DateTimeField(auto_now=True, verbose_name="评论时间")
    post = models.ForeignKey('blog.Post', on_delete=models.SET_NULL, null=True) # 外键关联blog APP 的数据库表Post;

    def __str__(self):
        return  self.text[:30]
