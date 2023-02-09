import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from shopping.models import Product

from .models import Cart, CartItem, UserProxy
from .utils import user_check


class CartListView(View):
    def get(self, request):
        userId = user_check(request)

        if request.user.is_anonymous:
            currentUser = UserProxy.objects.get_or_create(cookie=userId)[0]
            print("USER NOT LOGGED IN: " + str(currentUser.cookie))
        else:
            currentUser = UserProxy.objects.get_or_create(user=userId)[0]
            print("USER LOGGED IN: " + str(currentUser.user.username))

        cart = Cart.objects.get_or_create(user=currentUser)[0]
        cartItems = CartItem.objects.filter(cart=cart).order_by("product__name")
        order_total = sum([(item.product.price * item.quantity) for item in cartItems])

        context = {
            "cart_items": cartItems,
            "order_total": order_total,
        }

        return render(request, "pages/cart.html", context)


class CartUpdateView(View):
    def post(self, request):
        data = json.loads(request.body)
        productId = data["productId"]
        action = data["action"]
        print("Action", action)
        print("ProductId", productId)

        userId = user_check(request)

        if request.user.is_anonymous:
            currentUser = UserProxy.objects.get_or_create(cookie=userId)[0]
            print("USER NOT LOGGED IN: " + str(currentUser.cookie))
        else:
            currentUser = UserProxy.objects.get_or_create(user=userId)[0]
            print("USER LOGGED IN: " + str(currentUser.user.username))

        product = Product.objects.get(id=productId)

        cart = Cart.objects.get_or_create(user=currentUser)

        cartItem = CartItem.objects.get_or_create(cart=cart[0], product=product)[0]

        if action == "add":
            cartItem.quantity += 1
        elif action == "remove":
            cartItem.quantity = 0
        elif action == "decrease":
            cartItem.quantity -= 1

        cartItem.save()

        if cartItem.quantity <= 0:
            cartItem.delete()

        return JsonResponse("Item was added to cart", safe=False)


# Create your views here.
