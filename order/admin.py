from django.contrib import admin

from .models import Address, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "address",
        "cart",
        "status",
        "created_at",
        "modified_at",
        "delivered_at",
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(Address)
# Register your models here.
