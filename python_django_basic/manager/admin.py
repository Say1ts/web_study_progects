from django.contrib import admin

from .models import PdfFiles


class PdfFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(PdfFiles, PdfFilesAdmin)
