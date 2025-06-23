from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from catalog.models import Product
from django.contrib import messages

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_create(request):
    if request.method == 'POST':
        # здесь логика создания заказа из корзины (предположим, корзина — session)
        cart = request.session.get('cart', {})
        if not cart:
            messages.warning(request, "Корзина пуста.")
            return redirect('catalog:product_list')

        order = Order.objects.create(user=request.user)
        for product_id, quantity in cart.items():
            product = Product.objects.get(pk=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        request.session['cart'] = {}
        return redirect('orders:order_success')
    else:
        return redirect('catalog:product_list')


@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')
