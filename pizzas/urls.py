"""Defines URL patterns for pizzas"""
from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    #Page that shows all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    #Detail page for a single pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]