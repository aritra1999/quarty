from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

import requests

def home_view(request):

    context = {
        'title': 'Home',
    }

    if request.user.is_authneticated: 
        context['news'] = requests.get('https://newsapi.org/v2/top-headlines?q=covid&apiKey=5966c307d22e4a9caf56e4935632ea77').json()
        context['post_type'] = ["Blog", "Picture", "Lead Info", "Video", "GIFs"],
        context['posts'] = Post.objects.all().order_by('timestamp')


    return render(request, 'dashboard/home.html', context)


@login_required()
def add_post(request):
    context = {
        'title': 'Add Post'
    }
    return render(request, 'dashboard/add_post.html', context)
