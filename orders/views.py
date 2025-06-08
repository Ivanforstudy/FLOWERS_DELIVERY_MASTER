# orders/views.py

from django.shortcuts import render, redirect
from .models import Order, OrderItem
from catalog.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def order_create(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "Ваша корзина пуста.")
        return redirect('catalog:product_list')

    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)
            except Product.DoesNotExist:
                continue
        request.session['cart'] = {}
        messages.success(request, "Ваш заказ успешно создан.")
        return redirect('orders:order_success')

    return render(request, 'orders/order_create.html')
