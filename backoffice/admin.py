from django.contrib import admin
from .models import ProductType,ProductSubType,Product,ProductBrand,ProductImage,ProductLink,ProductReferences
from jet.admin import CompactInline
import copy

def duplicate_product(modeladmin, request, queryset):
    for p in queryset:
        pcopy=copy.copy(p)
        p.ProductName = p.ProductName + " - copie"
        p.pk=None
        p.save()
    duplicate_product.short_description ="Duplicate product"

class ProductBrandAdmin(admin.ModelAdmin):
    list_display=("pk","Name","OriginCountry","URL")
    list_display_links=("pk",)
    list_editable=("Name","OriginCountry","URL")

    def get_model_perms(self, request):
        return{}  

class ProductTypeAdmin(admin.ModelAdmin):
    list_display=("pk","Type",)
    list_display_links=("pk",)
    list_editable=("Type",)

    def get_model_perms(self, request):
        return{}    

class ProductSubTypeAdmin(admin.ModelAdmin):
    list_display=("pk","SubType",)
    list_display_links=("pk",)
    list_editable=("SubType",)

    def get_model_perms(self, request):
        return{}  

class ProductImageInline(CompactInline):
    model=ProductImage
    exclude = ('height','width')

class ProductLinkInline(CompactInline):
    model=ProductLink

class ProductReferencesInline(CompactInline):
    model=ProductReferences


class ProductAdmin(admin.ModelAdmin):
    actions = [duplicate_product]
    list_filter = ('Tags','ProductType','ProductSubType','Brand')#,'BuyPrice')
    search_fields = ['ProductName',]
    list_display=("ProductName","tag_list","ProductType","ProductSubType","Brand","get_MainProductBuyPrice","get_MainProductSellPrice","get_MainProductWeight")#,"BuyPrice","SellPrice","Weight")
    #inlines = (ProductImageInline,ProductLinkInline,)
    inlines = (ProductReferencesInline,ProductImageInline,ProductLinkInline)
    exclude=("Weight","BuyPrice","SellPrice")
    js=['tiny_mce/tiny_mce.js',]

    def get_queryset(self, request):
        return super(ProductAdmin, self).get_queryset(request).prefetch_related('Tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.Tags.all())

    def get_MainProductBuyPrice(self,obj):
        return obj.MainProductReference.BuyPrice
    #get_MainProductBuyPrice.admin_order_field="Référence - Prix d'achat"
    get_MainProductBuyPrice.short_description="Référence - Prix d'achat"

    def get_MainProductSellPrice(self,obj):
        return obj.MainProductReference.SellPrice
    #get_MainProductSellPrice.admin_order_field="Référence - Prix de vente"
    get_MainProductSellPrice.short_description="Référence - Prix de vente"

    def get_MainProductWeight(self,obj):
        return u"%s %s" % (obj.MainProductReference.Measure,obj.MainProductReference.MeasureUnit)
        #return obj.MainProductReference.Measure
    #get_MainProductWeight.admin_order_field="Référence - Poids"
    get_MainProductWeight.short_description="Référence - Poids"

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBrand,ProductBrandAdmin)
admin.site.register(ProductType,ProductTypeAdmin)
admin.site.register(ProductSubType,ProductSubTypeAdmin)