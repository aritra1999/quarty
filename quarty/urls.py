from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from dashboard.views import (
    home_view
)

from accounts.views import (
    profile_view
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),

    path('accounts/', include('allauth.urls')),
    path('profile/', profile_view, name="profile"),
    path('logout', LogoutView.as_view(), name='logout'),
]