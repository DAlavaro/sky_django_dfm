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
            {'title': 'product_one', 'description': 'description_one', 'category': category_one, 'price': 100},
            {'title': 'product_two', 'description': 'description_two', 'category': category_two, 'price': 200},
            {'title': 'product_three', 'description': 'description_three', 'category': category_three, 'price': 300},
            {'title': 'product_four', 'description': 'description_four', 'category': category_one, 'price': 400},
            {'title': 'product_five', 'description': 'description_five', 'category': category_two, 'price': 500},
            {'title': 'product_six', 'description': 'description_six', 'category': category_three, 'price': 600},
        ]

        product_for_create = []
        for item in product_list:
            created = Product.objects.create(**item)
            product_for_create.append(created)
