from app.blog.models import Blog
from app.catalog.models import Category, Product, Version
from django.core.management import BaseCommand


class Command(BaseCommand):
    # Clear existing records from the models
    Category.objects.all().delete()
    Product.objects.all().delete()
    Blog.objects.all().delete()
    Version.objects.all().delete()

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
            {'title': 'product_one', 'description': 'description_one', 'category': category_one, 'price': 100, 'photo': 'product/product_one.png'},
            {'title': 'product_two', 'description': 'description_two', 'category': category_two, 'price': 200, 'photo': 'product/product_two.png'},
            {'title': 'product_three', 'description': 'description_three', 'category': category_three, 'price': 300, 'photo': 'product/product_three.png'},
            {'title': 'product_four', 'description': 'description_four', 'category': category_one, 'price': 400, 'photo': 'product/product_four.png'},
            {'title': 'product_five', 'description': 'description_five', 'category': category_two, 'price': 500, 'photo': 'product/product_five.png'},
            {'title': 'product_six', 'description': 'description_six', 'category': category_three, 'price': 600, 'photo': 'product/product_six.png'},
        ]

        product_for_create = []
        for item in product_list:
            created = Product.objects.create(**item)
            product_for_create.append(created)

        blog_list = [
            {'title': 'blog_one', 'slug': 'blog_one','content': 'content_one', 'photo': 'blog/blog_one.png', 'is_published': True},
            {'title': 'blog_two', 'slug': 'blog_two','content': 'content_two', 'photo': 'blog/blog_two.png', 'is_published': True},
        ]

        blog_for_create = []
        for item in blog_list:
            created = Blog.objects.create(**item)
            blog_for_create.append(created)

        version_list = [
            {'product': product_for_create[0], 'number': 1, 'title': 'Version 1.0', 'is_active': True},
            {'product': product_for_create[0], 'number': 2, 'title': 'Version 2.0'},
            {'product': product_for_create[1], 'number': 1, 'title': 'Version 1.0', 'is_active': True},
            {'product': product_for_create[1], 'number': 2, 'title': 'Version 2.0'},
            {'product': product_for_create[2], 'number': 1, 'title': 'Version 1.0', 'is_active': True},
            {'product': product_for_create[2], 'number': 2, 'title': 'Version 2.0'},
        ]

        version_for_create = []
        for item in version_list:
            created = Version.objects.create(**item)
            version_for_create.append(created)

