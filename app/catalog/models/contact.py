from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Имя')
    email = models.EmailField(max_length=255, blank=False, null=False, verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'