from django.contrib import admin
from dizhi.models import Address
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display =['aname','aphone','asheng','acity','aqu','amenpai','abq']
    list_filter = ['aname']
    search_fields = ['aname']


admin.site.register(Address,AddressAdmin)

admin.site.site_tiitle='地址'