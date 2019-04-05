from django.db import models

# Create your models here.

# 关系: 书籍和英雄====一对多

class BookInfo(models.Model):
    # 默认会有主键， 为id并且自增
    # 书籍名称: 字符串区域
    btitle = models.CharField(max_length=50)
    # 书籍的出版日期, 相当于datetime.date.today()
    bpub_date = models.DateField()
    def __str__(self):
        return  'BookInfo %s' %(self.btitle)
class HeroInfo(models.Model):
    hname = models.CharField(max_length=30)
    hgender = models.BooleanField()
    hcontent = models.TextField()
    # 如果是Django1.x版本, models.ForeignKey(BookInfo);
    # 如果是Django2.x版本, models.ForeignKey(BookInfo);
    # models.CASCADE: 级联删除， 如果书籍删除了， 书籍里面的英雄也就删除了
    # models.DO_NOTHING: 当删除有关联的数据库内容是会报错
    # models.SET_NULL:不是级联删除， 如果书籍删除， 那么英雄所属的书籍为Null；
    # models.SET_DEFAULT：不是级联删除， 如果书籍删除， 那么英雄所属的书籍为默认值;
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return  'HeroInfo %s' %(self.hname)