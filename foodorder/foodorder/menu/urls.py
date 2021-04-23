from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mainpage,name='main_page'),
    path('orderpizza',views.pizzadashboard,name='pizza_dashboard'),
    path('orderburger',views.burgerdashboard,name='burger_dashboard'), 
    path('burger-type-cheese',views.cheeseburger,name='burger_type_1'),
    path('burger-type-paneer',views.paneerburger,name='burger_type_2'),
    path('burger-type-roasted',views.roastedburger,name='burger_type_3'),

    path('pizza-type-cheese',views.cheesepizza,name='pizza_type_1'),
    path('pizza-type-paneer',views.paneerpizza,name='pizza_type_2'),
    path('pizza-type-roasted',views.roastedpizza,name='pizza_type_3'),
]