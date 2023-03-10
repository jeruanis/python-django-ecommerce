from .models import Cart, CartItem
from .views import _cart_id
from accounts.models import Account
import json
import requests
from urllib.parse import urlparse
from decouple import config
from django.shortcuts import redirect
from django.core.cache import cache

def counter(request):
    cart_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)#total user cart_items
                for cart_item in cart_items:
                    cart_count += cart_item.quantity
            else:
                cart_items = CartItem.objects.all().filter(cart_id=cart[:1])#only need one result
                for cart_item in cart_items:
                    cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0

    return dict(cart_count=cart_count)


