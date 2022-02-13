from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

import requests


def home_view(request):
    context = {
        'title': 'Home',
        'post_type': ["Blog", "Picture", "Lead Info", "Video", "GIFs"],
    }

    if request.user.is_authenticated: 
        context['news'] = requests.get('https://newsapi.org/v2/top-headlines?q=covid&apiKey=5966c307d22e4a9caf56e4935632ea77').json()
        context['posts'] = Post.objects.all().order_by('-timestamp')

    return render(request, 'dashboard/home.html', context)


@login_required()
def add_post(request):
    context = {
        'title': 'Add Post'
    }

    if request.method == "POST":
        if request.POST.get('post_type') is None: 
            return redirect('/')
        Post.objects.create(
            title=request.POST.get('title'),
            type=request.POST.get('type'),
            user=request.user,
            thumbnail=request.FILES['thumbnail']
        ).save()

    return redirect('/')
