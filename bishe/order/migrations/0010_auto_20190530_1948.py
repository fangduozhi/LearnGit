# Generated by Django 2.1.7 on 2019-05-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20190521_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='oammount',
            field=models.CharField(max_length=40, verbose_name='总价'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ocount',
            field=models.IntegerField(verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='order',
            name='oprice',
            field=models.CharField(max_length=30, verbose_name='单价'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderid',
            field=models.CharField(max_length=50, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='oshopname',
            field=models.CharField(max_length=20, verbose_name='菜品名'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('wwc', '未完成'), ('ywc', '已完成')], default='未完成', max_length=10, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='下单时间'),
        ),
    ]