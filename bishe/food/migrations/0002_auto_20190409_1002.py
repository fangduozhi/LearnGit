# Generated by Django 2.1.7 on 2019-04-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_daily',
            name='ftype',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food_daily',
            name='gimg',
            field=models.ImageField(upload_to=''),
        ),
    ]