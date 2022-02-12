from email import message
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Message

from allauth.socialaccount.models import SocialAccount

@login_required
def chat_list(request): 
    context = {
        'title': 'Chat',
        'users': User.objects.all()
    }
    return render(request, 'chat/chat_list.html', context)


@login_required
def chat_view(request, message_to): 
    messages = (Message.objects.filter(message_to__username=request.user, message_from__username=message_to) | \
                Message.objects.filter(message_from__username=request.user, message_to__username=message_to)).order_by('timestamp')
    try: 
        message_to_pic = SocialAccount.objects.get(user__username=message_to).extra_data['picture']
    except:
        message_to_pic = ''

    context = {
        'title': "Chat with " + message_to,
        'message_to_pic': message_to_pic,
        'message_to': message_to,
        'room': str(max(message_to, request.user.username) + min(message_to, request.user.username)),
        'messages': messages
    }

    print('')
    return render(request, 'chat/chat.html', context)
