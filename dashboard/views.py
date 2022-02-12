from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


def home_view(request):
    context = {
        'title': 'Home',
        'post_type': ["Blog", "Picture", "Lead Info", "Video", "GIFs"],
        'posts': Post.objects.all().order_by('timestamp')
    }
    return render(request, 'dashboard/home.html', context)


@login_required()
def add_post(request):
    context = {
        'title': 'Add Post'
    }
    return render(request, 'dashboard/add_post.html', context)
