from django.core.management.base import BaseCommand
from products.models import Category, Product
from products import _crawler


class Command(BaseCommand):
    help = 'Save data of categories and products to db'

    def handle(self, *args, **kwargs):
        data = _crawler.crawl_product()
        for item in data:
            category = Category.objects.get_or_create(title=item[0])
            if type(category) == tuple:
                category = category[0]
            Product.objects.create(category=category, name=item[1], price=int(item[2].replace(',', '')), color=item[3],
                                   seller=item[4])
