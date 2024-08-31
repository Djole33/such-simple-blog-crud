from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

@login_required(login_url='login')
def post_details(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'main/post-details.html', {'post': post})

@login_required(login_url='login')
def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'main/add-post.html', {'form': form})

@login_required(login_url='login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'main/update-post.html', {'form': form})

@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')
