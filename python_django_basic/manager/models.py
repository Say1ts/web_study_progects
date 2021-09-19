from django.db import models


class PdfFiles(models.Model):
    title = models.CharField(max_length=40, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    file = models.FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['-created_at']
