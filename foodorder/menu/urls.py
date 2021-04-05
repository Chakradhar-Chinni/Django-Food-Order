from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mainpage,name='main_page'),
    path('orderpizza',views.pizzadashboard,name='pizza_dashboard'),
    path('orderburgger',views.burgerdashboard,name='burger_dashboard'),
]