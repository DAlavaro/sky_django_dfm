from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='product', verbose_name='Фото', **NULLABLE)
    category = models.ForeignKey('catalog.Category', on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='Цена', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', **NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.category})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
