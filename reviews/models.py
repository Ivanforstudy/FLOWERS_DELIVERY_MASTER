from django.db import models
from django.conf import settings
from catalog.models import Bouquet

class Review(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}⭐ от {self.user.username} для {self.bouquet.name}"
