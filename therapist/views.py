from django.shortcuts import render

# Create your views here.
def therapist(request):
    """A view to display therapist page"""
    return render(request, 'therapist/therapist.html')
