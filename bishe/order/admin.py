from django.contrib import admin

# Register your models here.
from order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['u_name','orderid','oshopname','oprice','ocount','oammount','time','state']
    search_fields = ['orderid']
    list_editable = ['state']


admin.site.register(Order,OrderAdmin)

admin.site.site_tiitle='订单'