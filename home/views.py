from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def blog(request):
    return render(request, "home/blog.html")

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST["name"],
            phone=request.POST["phone"],
            email=request.POST["email"],
            content=request.POST["content"]
        )
    return render(request, "home/contact.html")
