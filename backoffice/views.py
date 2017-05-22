from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product,ProductReferences,ProductImage,ProductType,ProductSubType,ProductBrand
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import QueryDict
from django.db.models import Q
from functools import reduce

# Create your views here.
def p_list(request):
    ## Récup des données ##
    p_list = Product.objects.all().order_by("ProductName")
    pt_list = ProductType.objects.all().order_by("Type")
    pst_list=ProductSubType.objects.all().order_by("SubType")
    pb_list=ProductBrand.objects.all().order_by("Name")
    #######################

    ## Search filter ##
    q=QueryDict(request.GET.get("q"))
    if q.__contains__("q_categorie"):
        q_categorie=q.getlist("q_categorie")
        p_list=Product.objects.filter(reduce(lambda x, y: x | y,[Q(ProductType__Type=item) for item in q_categorie]))
    if q.__contains__("q_subtypeproduct"):
        q_subtypeproduct=q.getlist("q_subtypeproduct")
        p_list=p_list.filter(reduce(lambda x, y: x | y,[Q(ProductSubType__SubType=item) for item in q_subtypeproduct]))
    if q.__contains__("q_brand"):
        q_brand=q.getlist("q_brand")
        p_list=p_list.filter(reduce(lambda x, y: x | y,[Q(Brand__Name=item) for item in q_brand]))
    ###################

    ## Ajout du tri ##
    p_list.order_by("ProductName")
    # à développer avec tri dynamique
    ##################

    ## Gestion de la pagination ##
    paginator = Paginator(p_list, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    ##############################
    return render(request, 'backoffice/p_list.html',{'products':products, 'ptypes':pt_list, 'psubtypes':pst_list, 'pbrands':pb_list})

def p_detail(request,pk):
    p=get_object_or_404(Product,pk=pk)
    p_photos=ProductImage.objects.filter(Product=p)
    p_refs=ProductReferences.objects.filter(Product=p)
    return render(request,'backoffice/p_detail.html',{'product':p, 'photos':p_photos, 'references':p_refs})