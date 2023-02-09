from django.db import models

from ecommerce.users.models import User
from shopping.models import Product


class UserProxy(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cookie = models.CharField(null=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(
        UserProxy, on_delete=models.CASCADE, related_name="user_cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.product.price * self.quantity

    # @property
    # def subtotal(self):
    #     order = self.product.all()
    #     total = sum([item.price for item in order])
    #     return total


# Create your models here.
