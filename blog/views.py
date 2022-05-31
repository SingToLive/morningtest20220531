from django.shortcuts import render, redirect
from .models import Article, Category

# Create your views here.
def new(request):
    all_ca = Category.objects.all()
    cat = []
    for ca in all_ca:
        cat.append(ca.name)
    return render(request, 'new.html', {'cate': cat})

def category(request):
    all_ca = Category.objects.all()
    print(all_ca)
    return render(request, 'category.html', {'cate': all_ca})