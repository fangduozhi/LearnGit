# Generated by Django 2.1.7 on 2019-04-09 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20190409_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_daily',
            name='ftype',
            field=models.CharField(choices=[('food_rc', '热菜'), ('food_lc', '凉菜')], max_length=30),
        ),
    ]
