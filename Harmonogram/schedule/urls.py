from . import views
from django.urls import path
# from .views import GetModelDataView

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('generate', views.generate, name='generate_home'),
    path('generate/<str:pk>/', views.generate, name='generate'),
    path('create_store/', views.createStore, name='crud'),
    path('update_store/<str:pk>/', views.updateStore, name='update_store'),
    path('delete_store/<str:pk>/', views.deleteStore, name='delete_store'),
    # path('get_model_data/', views.GetModelDataView.as_view(),
    #      name='get_model_data')

]
