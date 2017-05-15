from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def p_list(request):
    p_list = Product.objects.all()
    return render(request, 'backoffice/p_list.html',{'products':p_list})