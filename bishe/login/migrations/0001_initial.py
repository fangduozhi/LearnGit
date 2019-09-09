# Generated by Django 2.1.7 on 2019-04-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=15, verbose_name='用户名')),
                ('upassword', models.CharField(max_length=15, verbose_name='密码')),
                ('uphone', models.CharField(max_length=20, verbose_name='电话')),
            ],
        ),
    ]
