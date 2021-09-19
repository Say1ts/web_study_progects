from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about_developer(request):
    return render(request, 'about/about_dev.html')


def about_site(request):
    return render(request, 'about/about_site.html')
