from app.catalog.models import Category, Product
from django.core.management import BaseCommand


class Command(BaseCommand):
    # Clear existing records from the models
    Category.objects.all().delete()
    Product.objects.all().delete()

    def handle(self, *args, **options):
        category_one = Category.objects.create(
            title='category_one',
        )

        category_two = Category.objects.create(
            title='category_two',
        )

        category_three = Category.objects.create(
            title='category_three',
        )

        product_list = [
            {'title': 'product_one', 'category': category_one},
            {'title': 'product_two', 'category': category_two},
            {'title': 'product_three', 'category': category_three},
            {'title': 'product_four', 'category': category_one},
            {'title': 'product_five', 'category': category_two},
            {'title': 'product_six', 'category': category_three},
        ]

        product_for_create = []
        for item in product_list:
            created = Product.objects.create(**item)
            product_for_create.append(created)
