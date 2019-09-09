from django.db import models
from django.contrib import admin

# Create your models here.

class food_daily(models.Model):
    fid=models.AutoField(primary_key=True)
    fname=models.CharField(verbose_name='菜名',max_length=30)
    price=models.DecimalField(verbose_name='价格',max_digits=6,decimal_places=2)
    f_types=(
        ('food_rc','热菜'),
        ('food_lc','凉菜'),
        ('food_tg','汤羹'),
        ('food_zs','主食'),
        ('food_xc','小吃'),
        ('food_js','饮品酒水'),
        ('food_hx','海鲜')
    )
    ftype = models.CharField(verbose_name='菜系',choices=f_types,max_length=30)

    gimg=models.ImageField(upload_to='static/images',verbose_name='上传图片')
    class Meta:
        db_table='food_food_daily'
        verbose_name_plural='菜单管理'
    def __str__(self):
        return self.fname


