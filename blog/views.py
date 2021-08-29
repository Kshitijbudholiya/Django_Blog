from os import name
from django.core import paginator
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import blog, contact, comme
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
        return render(request, 'search_error.html')
    else:
        if(post.count()==0):
            return render(request, 'search_not_found.html', {"search": search_name})
        else:
            pagi = Paginator(post, 5)
            page_num = request.GET.get('page')
            page_obj = pagi.get_page(page_num)
            params = {"search": search_name, "posts": page_obj}
            return render(request, 'search.html', params)

def about(request):
    return render(request, "about.html")

def contact_us(request):
    return render(request, "contact.html")

def contact_save(request):
    name = request.POST['name']
    desc = request.POST['desc']
    email = request.POST['email']
    phone = request.POST['phone']
    #saving it
    contact_form = contact(name=name, desc=desc, email=email, phone=phone)
    contact_form.save()
    return render(request, 'save_cont.html')

def posts(request, post_id):
    post = blog.objects.all().filter(id=post_id)
    comments = comme.objects.all().filter(postid=post_id)
    print(comments)
    return render(request, 'post.html', {"post": post[0], "id": post_id, "comment": comments})

def comment(request):
    post_id = request.POST['post_id']
    comment = request.POST['comment']
    name = request.POST['name']
    #saving it
    comment_form = comme(postid=post_id, name=name, comment=comment)
    comment_form.save()
    return redirect('/post/'+post_id)
    