from django.db import models
from login.models import User
from food.models import food_daily
# Create your models here.

class Goods(models.Model):
    gid=models.AutoField(primary_key=True)
    sid=models.IntegerField()
    count=models.IntegerField()
    g_uname=models.CharField(max_length=10)
    class Meta:
        db_table='shopping_db'
