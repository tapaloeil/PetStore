import uuid
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from measurement.measures import Weight
from django_measurement.models import MeasurementField
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save,post_save
from django.db.models import Count
from django.utils.text import slugify
from model_utils import FieldTracker
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _

class ProductBrand(models.Model):
    Name=models.CharField(max_length=200,verbose_name='Marque')
    OriginCountry = CountryField(verbose_name="Pays d'origine")
    URL = models.URLField(max_length=1000,blank=True,null=True,verbose_name=('Liens vers le site'))

    class Meta:
        managed=True

    def __str__(self):
        return (self.Name)

class ProductType(models.Model):
    Type=models.CharField(max_length=200,verbose_name='Catégorie de produits')

    class Meta:
        managed=True

    def __str__(self):
        return self.Type

class ProductSubType(models.Model):
    SubType=models.CharField(max_length=200,verbose_name='Sous-atégorie de produits')

    class Meta:
        managed=True

    def __str__(self):
        return self.SubType

class ProductReferences(models.Model):
    Ref = models.CharField(max_length=200)
    BuyPrice = MoneyField(
        default=0,
        max_digits=10,
        decimal_places=2, 
        default_currency='EUR',
        blank=True,
        null=True,
        verbose_name="Prix d'achat (€)")
    SellPrice = MoneyField(
        default=0,
        max_digits=10,
        decimal_places=2, 
        default_currency='EUR',
        blank=True,
        null=True,
        verbose_name='Prix de vente (€)')
    MeasureUnitChoice =(
            ('g','g'),
            ('kg','kg'),
            ('ml','ml'),
            ('cl','cl'),
            ('l','l'),
        )
    MeasureUnit = models.CharField(max_length=3, choices=MeasureUnitChoice, default='g')
    Measure = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    Product=models.ForeignKey(
        'Product')
    class Meta:
        managed=True
        verbose_name="Reference"
        verbose_name_plural='References'

    def __str__(self):
        return self.Ref

class Product(models.Model):
    slug=models.SlugField(unique=True)
    ProductName=models.CharField(
        max_length=200,
        verbose_name='Nom du produit')
    ProductType=models.ForeignKey(
        'ProductType',
        on_delete=models.CASCADE,
        verbose_name='Catégorie de produit',
        db_index=True
        )
    ProductSubType=models.ForeignKey(
        'ProductSubType',
        on_delete=models.CASCADE,
        verbose_name='Type de produit',
        db_index=True
        )
    Brand=models.ForeignKey(
            'ProductBrand',
            on_delete=models.CASCADE,
            verbose_name='Marque',
            db_index=True
        )
    Description = HTMLField(
        blank=True,
        null=True)
    Tags=TaggableManager(blank=True)
    MainPhoto = models.ForeignKey(
        "ProductImage", related_name='+', blank=True, null=True,on_delete=models.SET_NULL
        )
    MainProductReference = models.ForeignKey(
        "ProductReferences", related_name='+',blank=True,null=True
        )
    Weight = MeasurementField(measurement=Weight,unit_choices=(("g","g"),("kg","kg")),null=True,blank=True, verbose_name="Poids (remplacé par Référence produit, à inactiver)")
    BuyPrice = MoneyField(
        max_digits=10,
        decimal_places=2, 
        default_currency='EUR',
        blank=True,
        null=True,
        verbose_name="Prix d'achat (remplacé par Référence produit, à inactiver)")
    SellPrice = MoneyField(
        max_digits=10,
        decimal_places=2, 
        default_currency='EUR',
        blank=True,
        null=True,
        verbose_name='Prix de vente (remplacé par Référence produit, à inactiver)')
    RefCount = models.SmallIntegerField(default=0,verbose_name="Références")
    tracker = FieldTracker()

    class Meta:
        managed=True

    def __str__(self):
        return self.ProductName

def upload_location(instance, filename):
    return "Product/%s/%s" %(instance.Product.pk,filename)

class ProductImage(models.Model):
    #image=models.ImageField(
    #    width_field="width",
    #    height_field="height",
    #    upload_to=upload_location
    #    )
    image=FilerImageField(
        related_name="product_image")
    height=models.IntegerField(default=0)
    width=models.IntegerField(default=0)
    Product=models.ForeignKey('Product')

    class Meta:
        managed=True
        verbose_name = "Images du produit"
        verbose_name_plural = "Images du produit"

class ProductLink(models.Model):
    Description = models.CharField(max_length=200)
    URL = models.URLField(
        max_length=3000,
        blank=True,
        null=True,
        verbose_name='Lien vers la fiche produit')
    Product=models.ForeignKey(
        'Product'
        )

    class Meta:
        managed=True
        verbose_name = "Liens vers les sites de vente"
        verbose_name_plural = "Liens vers les sites de vente"

    def __str__(self):
        return self.Description

def post_save_ProductImage_receiver(sender, instance, *args, **kwargs):
    if instance.image is not None and instance.Product.MainPhoto is None:
        instance.Product.MainPhoto=instance
        instance.Product.save()

def post_save_ProductReferences_receiver(sender, instance, *args, **kwargs):
    if instance.Product is not None and instance.Product.MainProductReference is None:
        instance.Product.MainProductReference=instance
    if instance.Product is not None:
        instance.Product.RefCount=ProductReferences.objects.filter(Product=instance.Product).count()
        instance.Product.save()

def create_slug(instance, new_slug=None):
    slug=slugify(instance.ProductName)
    if new_slug is not None:
        slug=new_slug
    qs=Product.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if(exists):
        new_slug="%s-%s" % (slug, str(uuid.uuid4())[:12])
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_Product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug or instance.tracker.has_changed("ProductName"):
        instance.slug=create_slug(instance)


post_save.connect(post_save_ProductImage_receiver, sender=ProductImage)
post_save.connect(post_save_ProductReferences_receiver, sender=ProductReferences)
pre_save.connect(pre_save_Product_receiver, sender=Product)