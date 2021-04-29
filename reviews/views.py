from django.shortcuts import render
from django.contrib import messages
from .models import Review
from django.conf import settings

from . import forms
from .forms import ReviewForm


def reviews(request):
    """A view to display a reviews page with all reviews from the DB """
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)

def write_review(request):
    """A view to display a form to Create a review"""
    form = ReviewForm

    context = {
        'form': form
    }
    return render(request, 'reviews/write_review.html', context)