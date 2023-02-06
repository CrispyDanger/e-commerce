import json

from .models import Cart, CartItem


def cart_items_fetch(request):
    current_user = request.user
    cartItemQuantity = 0
    if current_user.is_anonymous:
        print("USER IS NOT LOGGED IN")
        try:
            cart = json.loads(request.COOKIES["cart"])
        except json.JSONDecodeError:
            cart = {}
        print("Cart", cart)

        for item in cart:
            cartItemQuantity += cart[item]["quantity"]
        return {
            "cart_quantity": cartItemQuantity,
        }

    else:
        user_cart = Cart.objects.get_or_create(user=current_user)
        cartItemQuery = CartItem.objects.filter(cart=user_cart[0])
        cartItemQuantity = sum([cartItem.quantity for cartItem in cartItemQuery])
        return {
            "cart_quantity": cartItemQuantity,
        }
