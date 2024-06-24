
from django.core.management import BaseCommand

from app.users.models import Users


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = Users.objects.create(
            email='admin@sky.pro',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('admin')
        user.save()