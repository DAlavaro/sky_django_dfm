# Generated by Django 5.0.4 on 2024-06-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverificationtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailverificationtoken',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
