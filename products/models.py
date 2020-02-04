from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField()
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"my_id": self.id})
        # f"/products/{self.id}/"