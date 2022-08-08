from django.db import models

# Create your models here.
class Department(models.Model):
    '''部门表'''
    dname = models.CharField(verbose_name='部门名称', max_length=32)

class emp(models.Model):
    name = models.CharField(verbose_name='员工姓名', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    password = models.CharField(verbose_name='密码',max_length=32)
    account = models.DecimalField(verbose_name='账户余额', max_digits=10,decimal_places=2,default=0)
    hiretime = models.DateTimeField(verbose_name='入职时间')
    gender_choice = ((1,'男'),(2,'女'))
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choice)
    deptno = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
