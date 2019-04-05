from django.contrib import admin
from modelTest.models import  MyBook, Person, Group, GrouPersons
# Register your models here.


#
# class RelAdmin(admin.ModelAdmin):
#     list_display = [ 'date_joined', 'join_reason']



class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pubdate', 'read_num']
admin.site.register(MyBook, BookAdmin)
admin.site.register(Group)
admin.site.register(GrouPersons)
admin.site.register(Person)