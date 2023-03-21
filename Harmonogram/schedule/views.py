from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta


# Create your views here.

# def get_stores(request):
#     store_list = Store.objects.all()
#     return render(request, 'schedule.html', {'store_list': store_list})

def schedule(request):
    stores = Store.objects.all()
    in30days = Store.objects.filter(date_opening__gte=datetime.now(),
                                      date_opening__lt=datetime.now().date()
                                                       + timedelta(days=30))
    context = {'stores': stores, 'in30days': in30days}
    return render(request, 'schedule/schedule.html', context)


def generate(request):
    context = {}
    return render(request, 'schedule/generate.html', context)
