from django.shortcuts import render
from . models import *
from myBlog.models import *
from django.contrib import messages

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
            if len(request.POST["name"]) <= 2 or len(request.POST["phone"]) <= 9 or len(request.POST["email"]) <= 3 or len(request.POST["content"]) < 10:
                messages.error(request, "Please enter valid thing")
                # m = str({"message": "Please enter valid thing", "alert": "warning"})
                # messages.error(request, m)
            else:
                Contact.objects.create(
                    name=request.POST["name"],
                    phone=request.POST["phone"],
                    email=request.POST["email"],
                    content=request.POST["content"]
                )
                messages.success(request, "OK")
                # m = str({"message": "OK", "alert": "success"})
                # messages.success(request, m)

    return render(request, "home/contact.html")


def search(request):
    query = request.GET["q"]
    data1 = Post.objects.filter(title__icontains=query)
    data2 = Post.objects.filter(content__icontains=query)

    return render(request, "home/search.html", {"result": data1.union(data2), "query":query})

