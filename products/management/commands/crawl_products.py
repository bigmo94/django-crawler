from django.core.management.base import BaseCommand
from products.models import Category, Product
from products.management.commands import _crawler


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = _crawler.crawl_product()
        for item in data:
            category = Category.objects.get_or_create(title=item[0])
            if type(category) == tuple:
                category = category[0]
            Product.objects.create(category=category, name=item[1], price=item[2], color=item[3], seller=item[4])
