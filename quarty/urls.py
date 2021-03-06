from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from dashboard.views import (home_view, add_post)
from accounts.views import (profile_view)
from chat.views import (
    chat_list,
    chat_view
)
from recomendations.views import post_rec

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),

    path('accounts/', include('allauth.urls')),
    path('profile/<username>', profile_view, name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('chat/', chat_list, name='chat_list'),
    path('chat/<message_to>/', chat_view, name='chat'),

    path('rec/', post_rec, name='post_rec'),
    path('add_post/', add_post, name='add_post')
]