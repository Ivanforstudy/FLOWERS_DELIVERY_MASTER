from django.db import models
from django.utils import timezone

class DailyReport(models.Model):
    date = models.DateField(default=timezone.now, unique=True)
    total_orders = models.PositiveIntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Аналитика за {self.date}"
