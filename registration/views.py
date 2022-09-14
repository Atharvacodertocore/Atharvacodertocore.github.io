from django.shortcuts import render
from django.http import HttpResponse

def register_view(request, *args, **kwargs):
    return render(request, 'register.html')


# Create your views here.
