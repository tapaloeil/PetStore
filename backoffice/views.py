from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product,ProductReferences,ProductImage,ProductType,ProductSubType
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def p_list(request):
    p_list = Product.objects.all().order_by("ProductName")
    pt_list = ProductType.objects.all()
    pst_list=ProductSubType.objects.all()
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
    return render(request, 'backoffice/p_list.html',{'products':products, 'ptypes':pt_list, 'psubtypes':pst_list})

def p_detail(request,pk):
    p=get_object_or_404(Product,pk=pk)
    p_photos=ProductImage.objects.filter(Product=p)
    p_refs=ProductReferences.objects.filter(Product=p)
    return render(request,'backoffice/p_detail.html',{'product':p, 'photos':p_photos, 'references':p_refs})