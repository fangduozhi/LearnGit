# Generated by Django 2.1.7 on 2019-05-04 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='user',
        ),
        migrations.AddField(
            model_name='goods',
            name='g_uname',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]