from django.shortcuts import render, HttpResponse

from treatments.models import Treatment


def index(request):
    """A view to display index page"""
    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }
    return render(request, 'home/index.html', context)
