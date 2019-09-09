from django.contrib import admin


from food.models import food_daily

# Register your models here.
class food_dailyAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display =['fname','price','ftype']
    list_filter = ['ftype']
    search_fields = ['fname']
    list_editable = ['price']

admin.site.register(food_daily,food_dailyAdmin)
admin.site.site_header='菜单后台管理'
admin.site.site_tiitle='菜单'
