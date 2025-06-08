from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('', views.order_list, name='order_list'),  # если ты его добавил
    path('success/', views.order_success, name='order_success'),  # если нужен
]
