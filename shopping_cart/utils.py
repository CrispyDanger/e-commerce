from uuid import uuid4


def user_check(request):
    currentUser = request.user
    if currentUser.is_anonymous:
        print("USER IS NOT LOGGED IN")
        try:
            anonId = request.COOKIES["user"]
            print("Cart", anonId)
        except KeyError:
            anonId = uuid4()
        return anonId
    else:
        return currentUser
