from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from catalog.models import Bouquet

@login_required
def add_review(request, bouquet_id):
    bouquet = get_object_or_404(Bouquet, pk=bouquet_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.bouquet = bouquet
            review.save()
            return redirect('catalog:bouquet_detail', pk=bouquet.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {
        'form': form,
        'bouquet': bouquet
    })
