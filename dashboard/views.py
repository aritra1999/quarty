from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    constxt = {
        'title': 'Home'
    }
    return render(request, 'dashboard/home.html', {})



def add_post(request):
    context = {
        'title': 'Add Post' 
    }
    return render(request, 'dashboard/add_post.html', {})