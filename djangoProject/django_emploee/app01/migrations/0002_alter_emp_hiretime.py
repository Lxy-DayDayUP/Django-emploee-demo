# Generated by Django 4.0.6 on 2022-08-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='hiretime',
            field=models.DateField(verbose_name='入职时间'),
        ),
    ]
