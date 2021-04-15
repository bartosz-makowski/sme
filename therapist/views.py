from django.shortcuts import render


def therapist(request):
    """A view to display therapist page"""
    return render(request, 'therapist/therapist.html')
