from django.shortcuts import render
from django.http import HttpResponse

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html')

# Create your views here.
