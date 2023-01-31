from django.shortcuts import render

from .models import *


# Create your views here.

# def get_stores(request):
#     store_list = Store.objects.all()
#     return render(request, 'schedule.html', {'store_list': store_list})

def schedule(request):
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'schedule/schedule.html', context)

def generate(request):
    context = {}
    return render(request, 'schedule/generate.html', context)

