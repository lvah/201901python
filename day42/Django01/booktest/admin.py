from django.contrib import admin

# Register your models here.
# admin设置该APP后台管理的文件;


from booktest.models import BookInfo, HeroInfo
class HeroInfoAdmin(admin.ModelAdmin):

    list_display = ['hname', 'gender', 'hbook', 'hcontent']
    list_filter = ['hbook', 'hgender']
    search_fields = ['hname', 'hcontent']
    list_per_page = 5
    # 添加英雄时需要设置的属性及先后顺序；
    # fields = ['hname','hcontent', 'hgender']
    # 添加分组
    fieldsets = [
        ('必填内容', {'fields': ['hname', 'hbook']}),
        ('选填内容', {'fields': ['hgender', 'hcontent']})
    ]



# 创建书籍是内嵌的显示设置;这里是表格的内联；
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra =  2

class BookInfoAdmin(admin.ModelAdmin):
        inlines = [HeroInfoInline]

# 修改站点的头部信息和标题;
admin.site.site_header= "个人博客系统管理"
admin.site.site_title = "博客"

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
# admin.site.register(MyBook)
