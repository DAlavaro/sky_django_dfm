# Generated by Django 5.0.4 on 2024-04-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='slug'),
        ),
    ]
