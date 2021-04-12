from django.shortcuts import render, HttpResponse


def index(request):
    """A view to display index page"""
    
    return render(request, 'home/index.html')
