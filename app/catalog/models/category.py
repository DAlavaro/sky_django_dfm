from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
