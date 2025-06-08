from django.shortcuts import render
from catalog.models import Bouquet

def home_view(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'main/home.html', {'bouquets': bouquets})
