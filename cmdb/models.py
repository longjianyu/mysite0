from django.db import models

# Create your models here.

"""
创建两个字段，分别保存用户名和密码。
"""
class UserInfo(models.Model):#括号内，要继承models.Model类。固定写法
    user = models.CharField(max_length=32)#创建最大长度32，类型是char
    pwd = models.CharField(max_length=32)