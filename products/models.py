from django.db import models

from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)

    created_time = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

    is_enable = models.BooleanField(verbose_name=_('Is Enabled'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Product(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)
    color = models.CharField(verbose_name=_('color'), max_length=10)
    price = models.IntegerField(verbose_name=_('price'), default='')
    seller = models.CharField(verbose_name=_('seller'), max_length=50)
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE)

    created_time = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

    is_enable = models.BooleanField(verbose_name=_('Is Enabled'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
