# telegram_bot/urls.py
from django.urls import path
from . import views

app_name = 'telegram_bot'

urlpatterns = [
    # Заглушка для отображения, если нужно подключение
    path('', views.bot_status, name='bot_status'),
]
