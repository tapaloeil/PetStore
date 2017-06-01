from django.shortcuts import render, get_object_or_404, redirect
from cartsystem.cart import Cart
from backoffice.models import ProductReferences
from django.http import HttpResponse
from django.views.generic import RedirectView
from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json
#from django.views.decorators.csrf import ensure_csrf_cookie
#from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def add_to_cart(request, product_ref_id, quantity):
    product_ref=ProductReferences.objects.get(id=product_ref_id)
    cart=Cart(request)
    cart.add(product_ref, quantity)
    return HttpResponse('')

def remove_from_cart(request, product_ref_id):
    product_ref=ProductReferences.objects.get(id=product_ref_id)
    cart=Cart(request)
    cart.remove(product_ref)
    return redirect('get_cart')

def get_chart(request):
    return render(request, "cartsystem/cart.html", dict(cart=Cart(request)))


class api_add_to_cart(APIView):
    parser_classes=(JSONParser,)
    def get(self, request, format=None):
        data=request.GET
        cart=Cart(request)
        for product_ref_id, quantity in data.items():
            product_ref=ProductReferences.objects.get(id=product_ref_id)
            cart.add(product_ref, quantity)
        resp='{"cartItems":"' + str(cart.count()) + '"}'
        return Response(json.loads(resp))

class api_remove_from_cart(APIView):
    def get(self, request, format=None):
        #product_ref=ProductReferences.objects.get(id=product_ref_id)
        #cart=Cart(request)
        #cart.remove(product_ref)
        return Response(status = status.HTTP_200_OK)

class api_get_cart_count(APIView):
    def get(self, request, format=None):
        cart=Cart(request)
        resp='{"cartItems":"' + str(cart.count()) + '"}'
        return Response(json.loads(resp))

class api_sync_cart(APIView):
    parser_classer=(JSONParser,)
    def get(self,request,format=None):
        data=request.GET
        cart=Cart(request)
        for product_ref_id, quantity in data.items():
            product_ref=ProductReferences.objects.get(id=product_ref_id)
            if int(quantity) == 0:
                remove_from_cart(request, product_ref_id)
            else:
                cart.update(product_ref, quantity)
        resp='{"cartItems":"' + str(cart.count()) + '"}'
        return Response(json.loads(resp))