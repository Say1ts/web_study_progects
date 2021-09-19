from django.shortcuts import render
from django.http import HttpResponse

from .models import PdfFiles


def manager(request):
    pdfs = PdfFiles.objects.all
    return render(request, 'manager/index.html', {'pdfs': pdfs, 'title': 'Список документов'})
