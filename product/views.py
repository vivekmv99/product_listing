from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request,'category_table.html',context)