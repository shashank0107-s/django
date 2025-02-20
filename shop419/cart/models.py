from django.db import models

# Create your models here.
from mainapp.models import Product
from django.contrib.auth.models import User


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    data_added = models.DataField(auto_now_add=True)
    def __str__(self):
        return f"{self.product.name} - Count: {self.quantity}"
    def get_total_price(self):
        return self.quantity * self.product.price