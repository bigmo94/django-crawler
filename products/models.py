from django.db import models

from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Product(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)
    color = models.CharField(verbose_name=_('color'), max_length=10)
    price = models.IntegerField(verbose_name=_('price'))
    seller = models.CharField(verbose_name=_('seller'), max_length=50)
    category = models.ManyToManyField(Category)

    class Meta:
        db_table = 'product'
        verbose_name = _('product')
        verbose_name_plural = _('products')