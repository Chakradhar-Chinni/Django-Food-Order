from django.shortcuts import render
from django.http import HttpResponse
from .forms import BurgerSelection
from .models import PickBurger
# Create your views here.

def mainpage(request):
    #return HttpResponse("Main Page static data")
    return render(request,'welcome.html')

def pizzadashboard(request):
    return render(request,'pizzadashboard.html')
    #return HttpResponse("Pizza Dashboard")
def burgerdashboard(request):
     if request.method=='POST':
        form = BurgerSelection(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Order is Placed! Thanks for shopping with us</h1>")
     else:
      form = BurgerSelection()
     return render(request,'burgerdashboard.html',{'form':form})

def cheeseburger(request):
    if request.method=='POST':
        form = BurgerSelection(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Order is Placed! Thanks for shopping with us</h1>")
    else:
      form = BurgerSelection()
    return render(request,'cheeseburger.html',{'form':form})

def paneerburger(request):
    if request.method=='POST':
        form = BurgerSelection(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Order is Placed! Thanks for shopping with us</h1>")
    else:
      form = BurgerSelection()
    return render(request,'paneerburger.html',{'form':form})

def roastedburger(request):
    if request.method=='POST':
        form = BurgerSelection(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Order is Placed! Thanks for shopping with us</h1>")
    else:
      form = BurgerSelection()
    return render(request,'roastedburger.html',{'form':form})

def cheesepizza(request):
    if request.method=='POST':
        form = BurgerSelection(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Order is Placed! Thanks for shopping with us</h1>")
    else:
      form = BurgerSelection()
    return render(request,'cheesepizza.html',{'form':form})

def paneerpizza(request):
    if request.method=='POST':
        form = BurgerSelection(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Order is Placed! Thanks for shopping with us</h1>")
    else:
      form = BurgerSelection()
    return render(request,'paneerpizza.html',{'form':form})

def roastedpizza(request):
    if request.method=='POST':
        form = BurgerSelection(request.POST)
        if form.is_valid():
            form.save() # saves data to table
            return HttpResponse("<h1>Order is Placed! Thanks for shopping with us</h1>")
    else:
      form = BurgerSelection()
    return render(request,'roastedpizza.html',{'form':form})
    

    
