from django.db import models
from django.db.models.deletion import SET


class Category(models.Model):
    """ 分类表"""
    name = models.CharField(max_length=128)

    class Meta:
        app_label = 'app'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ 产品表"""
    name = models.CharField(max_length=128,)
    category = models.ForeignKey(
        Category, null=True, default=None, on_delete=SET(None))
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        app_label = 'app'

    def __str__(self):
        return self.name
