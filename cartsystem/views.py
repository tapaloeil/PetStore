from django.shortcuts import render, get_object_or_404, redirect
from cartsystem.cart import Cart
from backoffice.models import ProductReferences
from django.http import HttpResponse
# Create your views here.
def add_to_cart(request, product_ref_id, quantity):
    print("toto")
    product_ref=ProductReferences.objects.get(id=product_ref_id)
    cart=Cart(request)
    cart.add(product_ref, quantity)
    return HttpResponse('')

def remove_from_cart(request, product_ref_id):
    product_ref=ProductReferences.objects.get(id=product_ref_id)
    cart=Cart(request)
    cart.remove(product_ref)
    return HttpResponse('')

def get_chart(request):
    return render(request, "cartsystem/cart.html", dict(cart=Cart(request)))