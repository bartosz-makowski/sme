from django.shortcuts import render

def location(request):
    """A view to display a location page"""
    return render(request, 'location/location.html' )
