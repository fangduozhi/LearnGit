# Generated by Django 2.1.7 on 2019-07-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20190530_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderid',
            field=models.CharField(max_length=50, verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='u_name',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
    ]
