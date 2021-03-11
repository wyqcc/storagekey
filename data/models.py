import django.utils.timezone as timezone

from django.db import models


# Create your models here.
from user.models import User


class Data(models.Model):
    id = models.AutoField(verbose_name='序号', primary_key=True)
    user_id = models.ForeignKey(User,verbose_name='用户编号',on_delete=models.CASCADE)
    url_name = models.CharField(verbose_name='网站名', max_length=20, null=True)
    url = models.URLField(verbose_name='链接', null=True)
    user_name = models.CharField(verbose_name='用户名', max_length=20, null=True)
    user_password = models.CharField(verbose_name='密码', max_length=128, null=True)
    remarks = models.TextField(verbose_name='备注', null=True)
    establish_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    class Meta:
        db_table = 'data'
        verbose_name_plural = '数据'

    # def __str__(self):
    #     return self.id
