from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.bouquet_list, name='bouquet_list'),
    path('<int:pk>/', views.bouquet_detail, name='bouquet_detail'),
]
