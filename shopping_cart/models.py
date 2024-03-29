from django.db import models

from ecommerce.users.models import User
from shopping.models import Product


class UserProxy(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cookie = models.CharField(null=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if self.user is None:
            return self.cookie
        else:
            return self.user.username


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

    def __str__(self):
        return self.product.slug

    @property
    def total(self):
        return self.product.price * self.quantity


# Create your models here.
