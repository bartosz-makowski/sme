from django.shortcuts import render, HttpResponse

from deals.models import Deal
from reviews.models import Review


def index(request):
    """A view to display index page"""
    deals = Deal.objects.all()
    reviews = Review.objects.all()

    context = {
        'deals': deals,
        'reviews': reviews,
    }
    return render(request, 'home/index.html', context)
