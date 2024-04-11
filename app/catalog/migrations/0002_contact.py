# Generated by Django 5.0.1 on 2024-04-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]