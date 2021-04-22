from django.shortcuts import render

from .models import Review


def reviews(request):
    """A view to display a reviews page with all reviews from the DB """
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)
