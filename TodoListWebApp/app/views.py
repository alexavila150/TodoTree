"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Task

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    
    context = {
        'title' :   'Home Page',
        'year'  :   datetime.now().year,
    }

    return render(
        request,
        'app/index.html',
        context
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def tasks(request):
    assert isinstance(request, HttpRequest)
    
    tasks = Task.objects.all()

    context = {
        'title' :   'Tasks',
        'year'  :   datetime.now().year,
        'tasks' :   tasks,
    }

    return render(
        request,
        'app/tasks.html',
        context
    )