from django.db import models
from django.contrib.auth.models import User

# 资源类型
class SourceKind(models.Model):
    name = models.CharField('资源名', max_length=256, null=True, blank=True, default='')
    update = models.DateTimeField('更新时间', auto_now=True, null=True, blank=True)


class Source(models.Model):
    name = models.CharField('资源名', max_length=256, null=True, blank=True, default='')
    kind = models.ForeignKey(SourceKind, verbose_name='类型', related_name='kind', on_delete=models.SET_NULL,
                             null=True, blank=True)
    unit = models.CharField('单位', max_length=16, null=True, blank=True, default='')
    update = models.DateTimeField('更新时间', auto_now=True, null=True, blank=True)


class Province(models.Model):
    name = models.CharField('名字', max_length=32, null=True, blank=True, default='')
    update = models.DateTimeField('更新时间', auto_now=True, null=True, blank=True)


class Price(models.Model): 
    source = models.ForeignKey(Source, verbose_name='资源', related_name='source', on_delete=models.SET_NULL,
                               null=True, blank=True)
    price = models.DecimalField('价格', decimal_places=2, max_digits=6)
    day = models.DateField("日期", auto_now=False, auto_now_add=False)
    province = models.ForeignKey(Province, verbose_name='省份', related_name='province', on_delete=models.SET_NULL,
                                 null=True, blank=True)

    
