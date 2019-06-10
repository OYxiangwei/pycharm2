import time

from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "这是站头"
admin.site.site_title = "这是站标题"
admin.site.index_title= "这是首页标语"
class studentadmin(admin.ModelAdmin):
    pass

class teacheradmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ["name","course","getroomname","getcurtime"]
    search_fields = ["name"]
    fieldsets = (
        ("基本信息",{'fields':["name",]}),
        ("其他信息",{"fields":["course","room"]}),
    )

class classroomadmin(admin.ModelAdmin):
    pass

admin.site.register(models.Student,studentadmin)
admin.site.register(models.teacher,teacheradmin)
admin.site.register(models.classroom,classroomadmin)