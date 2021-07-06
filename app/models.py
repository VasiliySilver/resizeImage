from django.db import models


class Image(models.Model):
    """ Модель изображения """
    title = models.CharField(max_length=255, verbose_name='Заголовок изображения')
    image = models.ImageField(upload_to='image/%Y/%m/%d/')
    original_image = models.ImageField(upload_to='image/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-created_at']
