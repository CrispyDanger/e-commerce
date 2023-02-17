from django.db import models

from shopping_cart.models import Cart, UserProxy

# Create your models here.


class Address(models.Model):
    user = models.OneToOneField(
        UserProxy, on_delete=models.CASCADE, related_name="user_address"
    )
    address = models.TextField(null=False)
    city = models.TextField(null=False)
    cookie_email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.address + " , " + self.city


class Order(models.Model):
    class Status(models.TextChoices):
        NOT_ORDERED = "NO", ("Not Ordered")
        DELIVERING = "PR", ("Deliver in Process")
        DELIVERED = "DL", ("Delivered")

    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.NOT_ORDERED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateField(null=True)
    modified_at = models.DateTimeField(auto_now=True)
