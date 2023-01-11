from django.shortcuts import render

# Create your views here.


def schedule(request):
    context = {}
    return render(request, 'schedule/schedule.html', context)


def generate(request):
    context = {}
    return render(request, 'schedule/generate.html', context)

