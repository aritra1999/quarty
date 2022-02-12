from email import message
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def chat_list(request): 
    context = {
        'title': 'Chat',
        'users': User.objects.all()
    }
    return render(request, 'chat/chat_list.html', context)

@login_required
def chat_view(request, message_to): 
    context = {
        'title': message_to,
        'message_to': message_to,
        'room': str(max(message_to, request.user.username) + min(message_to, request.user.username))
    }
    return render(request, 'chat/chat.html', context)
