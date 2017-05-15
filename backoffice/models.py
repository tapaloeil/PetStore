from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from measurement.measures import Weight
from django_measurement.models import MeasurementField
from taggit.managers import TaggableManager

class ProductBrand(models.Model):
    Name=models.CharField(max_length=200,verbose_name='Marque', blank=True,null=True)
    OriginCountry = CountryField(verbose_name="Pays d'origine")
    URL = models.URLField(max_length=1000,blank=True,null=True,verbose_name='Liens vers le site')

    def __str__(self):
        return (self.Name)

class ProductType(models.Model):
    Type=models.CharField(max_length=200,verbose_name='Catégorie de produits',blank=True,null=True)

    def __str__(self):
        return self.Type

class ProductSubType(models.Model):
    SubType=models.CharField(max_length=200,verbose_name='Sous-atégorie de produits',blank=True,null=True)

    def __str__(self):
        return self.SubType

class Product(models.Model):
    ProductName=models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Nom du produit')
    ProductType=models.ForeignKey(
        'ProductType',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Catégorie de produit'
        )
    ProductSubType=models.ForeignKey(
        'ProductSubType',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Type de produit'
        )
    Brand=models.ForeignKey(
            'ProductBrand',
            on_delete=models.CASCADE,
            blank=True,
            null=True,
            verbose_name='Marque'
        )
    Description = HTMLField(
        blank=True,
        null=True)
    Tags=TaggableManager(blank=True)
    MainPhoto = models.ForeignKey(
        "ProductImage", related_name='+', blank=True, null=True
        )
    #Weight = models.DecimalField(
    #    max_digits=10,
    #    decimal_places=2,
    #    blank=True,
    #    null=True,
    #    verbose_name='Poids en kg')
    Weight = MeasurementField(measurement=Weight,unit_choices=(("g","g"),("kg","kg")),null=True,blank=True)
    BuyPrice = MoneyField(
        max_digits=10,
        decimal_places=2, 
        default_currency='EUR',
        blank=True,
        null=True,
        verbose_name="Prix d'achat (€)")
    SellPrice = MoneyField(
        max_digits=10,
        decimal_places=2, 
        default_currency='EUR',
        blank=True,
        null=True,
        verbose_name='Prix de vente (€)')

    def __str__(self):
        return self.ProductName

def upload_location(instance, filename):
    return "Product/%s/%s" %(instance.Product.pk,filename)

class ProductImage(models.Model):
    image=models.ImageField(
        null=True,
        blank=True,
        width_field="width",
        height_field="height",
        upload_to=upload_location
        )
    height=models.IntegerField(default=0)
    width=models.IntegerField(default=0)
    Product=models.ForeignKey('Product',blank=True,null=True)

class ProductLink(models.Model):
    Description = models.CharField(max_length=200, blank=True, null=True)
    URL = models.URLField(
        max_length=3000,
        blank=True,
        null=True,
        verbose_name='Lien vers la fiche produit')
    Product=models.ForeignKey(
        'Product',
        blank=True,
        null=True
        )
    LinkBuyPrice= MoneyField(
        max_digits=10,
        decimal_places=2, 
        default_currency='EUR',
        default=0,
        verbose_name="Prix d'achat")