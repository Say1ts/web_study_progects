# Generated by Django 3.1.5 on 2021-01-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pdffiles',
            options={'ordering': ['-created_at'], 'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterField(
            model_name='pdffiles',
            name='content',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pdffiles',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='pdffiles',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='pdffiles',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]
