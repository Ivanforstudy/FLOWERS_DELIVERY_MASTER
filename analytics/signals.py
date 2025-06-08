from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from .models import DailyReport
from django.utils.timezone import localdate

@receiver(post_save, sender=Order)
def update_daily_report(sender, instance, created, **kwargs):
    if created and instance.status != 'cancelled':
        report, _ = DailyReport.objects.get_or_create(date=localdate())
        report.total_orders += 1
        report.total_revenue += instance.total_price
        report.save()
