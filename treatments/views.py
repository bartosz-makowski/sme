from django.shortcuts import render


def treatments(request):
    """A view to display available treatments and their details"""
    return render(request, 'treatments/treatments.html')
