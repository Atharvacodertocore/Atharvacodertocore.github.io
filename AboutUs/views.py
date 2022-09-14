from django.shortcuts import render
from django.http import HttpResponse

def about_view(request, *args, **kwargs):
    return render(request, 'about.html')


# Create your views here.
