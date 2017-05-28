from django.db import models
from backoffice.models import ProductReferences
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    creation_date=models.DateTimeField(verbose_name=_("creation date"))
    checked_out=models.BooleanField(default=False,verbose_name=_("checked out ?"))
    locale = models.CharField(max_length=10,default=get_language())

    class Meta:
        verbose_name=_("cart")
        verbose_name_plural=_("carts")
        ordering=("-creation_date",)

    def __str__(self):
        return(self.creation_date)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart, verbose_name=_("cart"))
    quantity=models.PositiveIntegerField(verbose_name=_("Quantité"))
    product_ref=models.ForeignKey(ProductReferences)

    class Meta:
        verbose_name=_("item")
        verbose_name_plural=_("items")
        ordering=('cart',)

    def __str__(self):
        return u'%d x %s' % (self.quantity,self.product_ref.Ref)

    def total_price(self):
        return self.quantity * self.product_ref.SellPriceRMB