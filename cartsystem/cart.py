import datetime
from . import models
import decimal

CART_ID="CART_ID"

class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart:
    def __init__(self,request):
        cart_id=request.session.get(CART_ID)
        if cart_id:
            try:
                cart=models.Cart.objects.get(id=cart_id,checked_out=False)
            except models.Cart.DoesNotExist:
                cart=self.new(request)
        else:
            cart=self.new(request)
        self.cart=cart

    def __iter__(self):
        #for field in models.self._meta.get_fields():
        #    print(field.name)
        #items=models.CartItem.objects.filter(cart=self)
        for item in self.cart.cartitem_set.all():
            yield item


    def new(self,request):
        cart=models.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID]=cart.id
        return cart

    def add(self,product_ref,quantity=1):
        try:
            item=models.CartItem.objects.get(
                cart=self.cart,
                product_ref=product_ref,
                )
        except models.CartItem.DoesNotExist:
            item=models.CartItem()
            item.cart=self.cart
            item.product_ref=product_ref
            item.quantity=quantity
            item.save()
        else:
            item.quantity += int(quantity)
            item.save()

    def remove(self,product_ref):
        try:
            item=models.CartItem.objects.get(
                cart=self.cart,
                product_ref=product_ref,
                )
        except models.CartItem.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self,product_ref,quantity):
        try:
            item=models.CartItem.objects.get(
                cart=self.cart,
                product_ref=product_ref,
                )
        except models.CartItem.DoesNotExist:
            raise ItemDoesNotExist
        else:
            if quantity==0:
                item.delete()
            else:
                item.quantity = int(quantity)
                item.save()
    def count(self):
        result=0
        for item in self.cart.cartitem_set.all():
            result+=1*item.quantity
        return result

    def summary(self):
        result=decimal.Decimal('0.0')
        for item in self.cart.cartitem_set.all():
            result = result + decimal.Decimal(item.total_price())
        return result

    def clear(self):
        for item in self.cart.cartitem_set.all():
            item.delete()