from django.shortcuts import render, HttpResponse

from treatments.models import Treatment
from reviews.models import Review


def index(request):
    """A view to display index page"""
    treatments = Treatment.objects.all()
    reviews = Review.objects.all()

    context = {
        'treatments': treatments,
        'reviews': reviews,
    }
    return render(request, 'home/index.html', context)
