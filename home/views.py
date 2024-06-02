from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def flavorShop(request):
    return render(request, "flavorShop.html")

def contact(request):
     if request.method == 'POST':
         name = request.POST.get('name')
         phone = request.POST.get('phone')
         email = request.POST.get('email')
         desc = request.POST.get('desc')
         
         contact = Contact(name = name, phone = phone, email = email, desc = desc, date = datetime.today())
         contact.save()

     return render(request, "contact.html")


