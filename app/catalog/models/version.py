from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Version(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='Продукт', **NULLABLE)
    number = models.PositiveIntegerField(verbose_name='Номер версии', **NULLABLE)
    title = models.CharField(max_length=255, verbose_name='Название версии', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активная версия', **NULLABLE)

    def __str__(self):
        return f'{self.product} ({self.number})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

