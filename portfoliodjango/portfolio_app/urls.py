from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("", views.base, name='base'),
    path("todos/", views.todos, name='Todos'),
    path("portfolio/", views.portfolio, name='Portfolio'),
]