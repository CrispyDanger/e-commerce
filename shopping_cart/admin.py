from django.contrib import admin

from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "cart", "created_at")


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

# Register your models here.
