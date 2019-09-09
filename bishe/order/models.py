from django.db import models
from django.contrib import admin
# Create your models here.
class Order(models.Model):
    oid=models.AutoField(primary_key=True)
    u_name=models.CharField(max_length=20,verbose_name='用户名')
    states=(
        ('未完成','未完成'),
        ('已完成','已完成')
    )
    o_img=models.ImageField()
    orderid = models.CharField(max_length=50,verbose_name='订单编号')
    state=models.CharField(default='未完成',max_length=10,verbose_name='订单状态',choices=states)
    oshopname=models.CharField(max_length=20,verbose_name='菜品名')
    oprice=models.CharField(max_length=30,verbose_name='单价')
    ocount=models.IntegerField(verbose_name='数量')
    oammount=models.CharField(max_length=40,verbose_name='总价')
    time=models.DateTimeField(auto_now=True,verbose_name='下单时间')

    class Meta:
        db_table='order_db'
        verbose_name_plural = '订单管理'