from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'accounts/profile.html', context)
