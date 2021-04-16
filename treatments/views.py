from django.shortcuts import render

from .models import Treatment


def treatments(request):
    """A view to display available treatments and their details"""
    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }
    return render(request, 'treatments/treatments.html', context)
