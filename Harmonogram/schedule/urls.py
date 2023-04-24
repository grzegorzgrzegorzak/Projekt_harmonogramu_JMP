from . import views
from django.urls import path

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('generate', views.generate, name='generate_home'),
    path('generate/<str:pk>/', views.generate, name='generate'),
    path('crud/', views.createStore, name='crud'),

]