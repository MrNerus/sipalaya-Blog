from django.shortcuts import render
from . models import *
from myBlog.models import *

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def blog(request):
    
    allPost = Post.objects.all()
    return render(request, 'home/blog.html', {'allpost':allPost})

def blogPost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    content={'post':post}
    return render(request, 'home/blogpost.html', content)
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST["name"],
            phone=request.POST["phone"],
            email=request.POST["email"],
            content=request.POST["content"]
        )
    return render(request, "home/contact.html")
