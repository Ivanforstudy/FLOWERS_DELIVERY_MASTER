from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<int:bouquet_id>/add/', views.add_review, name='add_review'),
]
