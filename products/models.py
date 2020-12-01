from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='No description available for this product.')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("products-detail", kwargs={"product_id": self.id})
