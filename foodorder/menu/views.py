from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainpage(request):
    #return HttpResponse("Main Page static data")
    return render(request,'welcome.html')
def pizzadashboard(request):
    return render(request,'pizzadashboard.html')
    #return HttpResponse("Pizza Dashboard")
def burgerdashboard(request):
    return render(request,'burgerdashboard.html')
