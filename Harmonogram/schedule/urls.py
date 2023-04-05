from . import views
from django.urls import path

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('generate/<str:pk>/', views.generate, name='generate')
]