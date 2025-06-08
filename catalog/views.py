from django.shortcuts import render, get_object_or_404
from .models import Bouquet

def bouquet_list(request):
    bouquets = Bouquet.objects.all()
    return render(request, 'catalog/bouquet_list.html', {'bouquets': bouquets})

def bouquet_detail(request, pk):
    bouquet = get_object_or_404(Bouquet, pk=pk)
    return render(request, 'catalog/bouquet_detail.html', {'bouquet': bouquet})
