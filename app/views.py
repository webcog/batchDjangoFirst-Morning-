from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# HTTPRespone > 
#  django.http > httpsr
# msg display web page

# request 

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")