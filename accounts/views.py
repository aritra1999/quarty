from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from dashboard.models import Post


@login_required
def profile_view(request, username):
    user = User.objects.get(username=username)
    try:
        profile = Profile.objects.get(user__username=username)
    except:
        return render(request, 'base/404.html', {})
    context = {
        'title': user.first_name + " " + user.last_name,
        'profile': Profile.objects.get(user__username=username),
        'posts': Post.objects.filter(user__username=username).order_by('-timestamp')
    }
    return render(request, 'accounts/profile.html', context)
