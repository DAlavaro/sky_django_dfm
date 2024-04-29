from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Имя')
    phone = models.CharField(max_length=255, verbose_name='Телефон', **NULLABLE)
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
