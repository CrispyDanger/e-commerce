from .models import Cart, CartItem, UserProxy
from .utils import user_check


def cart_items_fetch(request):
    cartItemQuantity = 0
    userId = user_check(request)

    if request.user.is_anonymous:
        user = UserProxy.objects.get_or_create(cookie=userId)[0]
        print("USER NOT LOGGED IN: " + str(user.cookie))
    else:
        user = UserProxy.objects.get_or_create(user=userId)[0]
        print("USER LOGGED IN: " + str(user.user.username))

    user_cart = Cart.objects.get_or_create(user=user)
    cartItemQuery = CartItem.objects.filter(cart=user_cart[0])
    cartItemQuantity = sum([cartItem.quantity for cartItem in cartItemQuery])
    return {
        "CookieValue": userId,
        "cart_quantity": cartItemQuantity,
    }
