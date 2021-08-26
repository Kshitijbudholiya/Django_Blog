from os import name
from django.core import paginator
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import blog
from math import ceil
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    post = blog.objects.all().order_by('id')
    pagi = Paginator(post, 5)
    page_num = request.GET.get('page')
    page_obj = pagi.get_page(page_num)
    params = {"posts": page_obj,}
    return render(request, 'index.html', params)

def search(request):
    search_name = request.GET.get('search')
    post = blog.objects.filter(Q(title__icontains=search_name)).order_by('id')
    if(search_name==""):
        return HttpResponse("Kuch To Likh")
    else:
        if(post.count()==0):
            return HttpResponse("Nahi Hai")
        else:
            pagi = Paginator(post, 5)
            page_num = request.GET.get('page')
            page_obj = pagi.get_page(page_num)
            params = {"search": search_name, "posts": page_obj}
            return render(request, 'search.html', params)