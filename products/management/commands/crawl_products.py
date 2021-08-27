from django.core.management.base import BaseCommand
from products.models import Category, Product
from _crawler import get_categories

class Command(BaseCommand):
    pass