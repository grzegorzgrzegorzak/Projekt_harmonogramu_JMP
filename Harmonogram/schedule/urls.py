from . import views
from django.urls import path

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('generate', views.generate, name='generate_home'),
    path('generate/<str:pk>/', views.generate, name='generate'),
    path('create_store/', views.createStore, name='crud'),
    path('update_store/<str:pk>/', views.updateStore, name='update_store'),
    path('delete_store/<str:pk>/', views.deleteStore, name='delete_store'),
    path('json_view/', views.json_view, name='json_view')
]