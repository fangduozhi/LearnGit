
from django.db import models

# Create your models here.
class Address(models.Model):
    aid=models.AutoField(primary_key=True)
    aname=models.CharField(verbose_name='用户名',max_length=15)
    aphone=models.CharField(verbose_name='电话',max_length=20)
    asheng=models.CharField(verbose_name='省份/自治区',max_length=30)
    acity=models.CharField(verbose_name='城市/地区',max_length=50)
    aqu=models.CharField(verbose_name='区/县',max_length=40)
    amenpai=models.CharField(verbose_name='街道地址，门牌',max_length=50)
    abq=models.CharField(verbose_name='标签',max_length=20)

    class Meta:
        db_table='address_user'
        verbose_name_plural='地址管理'