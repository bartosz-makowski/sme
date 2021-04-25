from django.shortcuts import render, HttpResponse


from deals.models import Deal
from reviews.models import Review
from .models import Location


def index(request):
    """A view to display index page"""
    deals = Deal.objects.all()
    reviews = Review.objects.all()
    locations = Location.objects.all()

    context = {
        'deals': deals,
        'reviews': reviews,
        'locations': locations
    }
    return render(request, 'home/index.html', context)
