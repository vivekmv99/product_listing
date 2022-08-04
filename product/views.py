from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.db.models import Avg, Sum

def index(request):
    category = Category.objects.filter(is_active=True)
    cat_list = []
    for i in category:
        product_count = Products.objects.filter(category=i.id).count()
        product_avg = Products.objects.filter(category=i.id).aggregate(Avg('price'))
        value = {
            'name':i.name,
            'id':i.id,
            'pro_count':product_count,
            'pro_avg':product_avg,
        }
        cat_list.append(value)
    context = {'category': cat_list}
    return render(request,'category_table.html',context)

def pro_list(request,pk):
    product = Products.objects.filter(category=pk)
    context = {'product':product}
    return render(request,'pro_list.html',context)