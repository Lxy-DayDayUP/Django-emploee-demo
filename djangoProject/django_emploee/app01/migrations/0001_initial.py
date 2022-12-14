# Generated by Django 4.0.6 on 2022-07-25 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=32, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='员工姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账户余额')),
                ('hiretime', models.DateTimeField(verbose_name='入职时间')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department')),
            ],
        ),
    ]
