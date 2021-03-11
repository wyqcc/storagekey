from django.db import models
import random
import django.utils.timezone as timezone


def default_department():
    department = ['研发部', '采购部', '销售部', '管理层']
    return random.choice(department)


# Create your models here.
class User(models.Model):
    user_id = models.AutoField('用户id', primary_key=True)
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码", null=False)
    name = models.CharField(max_length=20, verbose_name="姓名", null=True)
    phone = models.CharField(max_length=11, default='', null=True)
    email = models.EmailField(verbose_name="邮箱", null=True)
    department = models.CharField(default=default_department(), verbose_name='部门', max_length=20, null=True)
    user_type = models.CharField(verbose_name='用户类型', max_length=5, null=True)
    establish_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    old_time = models.DateTimeField(verbose_name='上次登录时间', null=True)

    class Meta:
        db_table = 'user'
        verbose_name_plural = '站点用户'

    def __str__(self):
        return self.username
