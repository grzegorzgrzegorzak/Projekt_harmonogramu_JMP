from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from datetime import datetime, timedelta
import freezegun
from .forms import StoreForm


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


#dopisać ifa gdy nie ma paramteru pk
def generate(request, pk=None):
    if pk is None:
        return render(request, 'schedule/generate.html')
    else:
        store = Store.objects.get(id=pk)
        contex = {'store': store}
        return render(request, 'schedule/generate.html', contex)


def createStore(request):

    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'schedule/crud.html', context)

def updateStore(request, pk):

    store = Store.objects.get(id=pk)
    form = StoreForm(instance=store)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'schedule/crud.html', context)

def deleteStore(request, pk):

    store = Store.objects.get(id=pk)
    context = {}
    return render(request, 'schedule/delete.html', context)