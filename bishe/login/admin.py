from django.contrib import admin
from login.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display =['uname','upassword','uphone']
    list_filter = ['uname']
    search_fields = ['uname']
admin.site.register(User,UserAdmin)
admin.site.site_header='餐厅后台管理系统'