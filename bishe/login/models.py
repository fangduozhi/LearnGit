from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(verbose_name='用户名',max_length=15)
    upassword=models.CharField(verbose_name='密码',max_length=15)
    uphone=models.CharField(verbose_name='电话',max_length=20)

    class Meta:
        db_table='login_user'
        verbose_name_plural='用户管理'


