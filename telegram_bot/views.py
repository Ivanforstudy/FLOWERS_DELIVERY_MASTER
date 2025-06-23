from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from orders.models import Order, OrderItem
from catalog.models import Product
from django.contrib.auth.models import User

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            message = data.get('message', {})
            chat_id = message.get('chat', {}).get('id')
            text = message.get('text', '')

            # Заглушка для теста: создаем пользователя и тестовый заказ
            if text.lower().startswith('/start'):
                User.objects.get_or_create(username=f'tg_{chat_id}', defaults={'password': 'unused'})
                response_message = 'Добро пожаловать! Введите название букета и адрес доставки.'
            else:
                # Примерная логика оформления заказа
                username = f'tg_{chat_id}'
                user, _ = User.objects.get_or_create(username=username)
                bouquet_name = text.strip()

                product = Product.objects.filter(name__icontains=bouquet_name).first()
                if product:
                    order = Order.objects.create(user=user)
                    OrderItem.objects.create(order=order, product=product, quantity=1)
                    response_message = f'Ваш заказ "{product.name}" принят!'
                else:
                    response_message = 'Букет не найден. Попробуйте снова.'

            return JsonResponse({"ok": True, "message": response_message})

        except Exception as e:
            return JsonResponse({"ok": False, "error": str(e)})

    return JsonResponse({"ok": False, "message": "Method not allowed"})
