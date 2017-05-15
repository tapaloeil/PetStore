from django.contrib import admin
from .models import ProductType,ProductSubType,Product,ProductBrand,ProductImage,ProductLink
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

class ProductLinkInline(CompactInline):
    model=ProductLink

class ProductAdmin(admin.ModelAdmin):
    actions = [duplicate_product]
    list_filter = ('Tags','ProductType','ProductSubType','Brand','BuyPrice')
    search_fields = ['ProductName',]
    list_display=("ProductName","tag_list","ProductType","ProductSubType","Brand","BuyPrice","SellPrice","Weight")
    inlines = (ProductImageInline,ProductLinkInline,)
    js=['tiny_mce/tiny_mce.js',]

    def get_queryset(self, request):
        return super(ProductAdmin, self).get_queryset(request).prefetch_related('Tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.Tags.all())


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBrand,ProductBrandAdmin)
admin.site.register(ProductType,ProductTypeAdmin)
admin.site.register(ProductSubType,ProductSubTypeAdmin)