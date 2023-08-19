from django.shortcuts import render
# Create your views here.

# HTTPRespone > 
#  django.http > httpsr
# msg display web page

# request 

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')