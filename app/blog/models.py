from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, unique=True,db_index=True, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    photo = models.ImageField(upload_to='blog', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'