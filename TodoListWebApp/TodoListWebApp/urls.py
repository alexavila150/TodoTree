"""
Definition of urls for TodoListWebApp.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
