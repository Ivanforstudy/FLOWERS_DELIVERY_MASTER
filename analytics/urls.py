from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.report_list, name='report_list'),
]
