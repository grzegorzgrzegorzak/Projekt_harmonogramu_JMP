from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from datetime import datetime, timedelta
import freezegun


# Create your views here.

# def get_stores(request):
#     store_list = Store.objects.all()
#     return render(request, 'schedule.html', {'store_list': store_list})

@freezegun.freeze_time('2022-02-13 00:00:00', tick=True)
def schedule(request):
    stores = Store.objects.all()
    in30days = Store.objects.filter(
        date_start_installation__gte=datetime.now().date(),
        date_start_installation__lt=datetime.now().date()
                                    + timedelta(days=30)).count()
    inrealization = Store.objects.filter(
        date_start_installation__lte=datetime.now().date(),
        date_opening__gt=datetime.now().date()).count()
    context = {'stores': stores, 'in30days': in30days,
               'inrealization': inrealization}
    return render(request, 'schedule/schedule.html', context)


def generate(request, pk=None):
    store = Store.objects.get(id=pk)
    contex = {'store': store}
    return render(request, 'schedule/generate.html', contex)

# def generate(request, pk):
#
#     if not pk:
#         return redirect(reverse('generate'))
#     try:
#         store = Store.objects.get(id=pk)
#     except Store.DoesNotExist:
#         context = {'store': store, 'pk': pk}
#         return render(request, '404.html', context, status=404)
#     context = {'store': store, 'pk': pk}
#     return render(request, 'schedule/generate.html', context)
