# Generated by Django 3.1.2 on 2020-10-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemain', '0004_auto_20201028_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
