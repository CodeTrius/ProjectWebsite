from django.shortcuts import render,HttpResponse
from .models import TodoItem
def home(request):
    return render(request,"home.html")

def base(request):
    return render(request,"base.html")

def portfolio(request):
    return render(request, "portfolio.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {"todos": items})