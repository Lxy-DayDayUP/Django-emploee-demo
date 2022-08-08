from django.db import models
# Create your models here.
class Department(models.Model):
    '''部门表'''
    dname = models.CharField(verbose_name='部门名称', max_length=32)

    def __str__(self):
        return self.dname

class emp(models.Model):
    name = models.CharField(verbose_name='员工姓名', max_length=32,)
    age = models.IntegerField(verbose_name='年龄')
    password = models.CharField(verbose_name='密码',max_length=32)
    account = models.DecimalField(verbose_name='账户余额', max_digits=10,decimal_places=2,default=0)
    hiretime = models.DateField(verbose_name='入职时间')
    gender_choice = ((1,'男'),(2,'女'))
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choice)
    deptno = models.ForeignKey(verbose_name='部门',to='Department', to_field='id', on_delete=models.CASCADE)

class niceNum(models.Model):
    num = models.CharField(verbose_name='靓号',max_length=11)
    price = models.DecimalField(verbose_name='价格',max_digits=10,decimal_places=2)
    level_choice=((1,'普通靓号'),(2,'高级靓号'),(3,'极品靓号'))
    level = models.SmallIntegerField(verbose_name='靓号级别',choices=level_choice,default=1)
    status_choice=((1,'未占用'),(2,'已占用'))
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choice,default=2)

class Admin(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=32)
    def __str__(self):
        return self.username
class Task(models.Model):
    level_choices = ((1,'紧急'),(2,'重要'),(3,'临时'))
    title = models.CharField(verbose_name='标题',max_length=64)
    detail = models.TextField(verbose_name='详细信息')
    level = models.SmallIntegerField(verbose_name='级别',choices=level_choices)
    user = models.ForeignKey(verbose_name='负责人',to='Admin',on_delete=models.CASCADE)