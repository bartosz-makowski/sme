from django.shortcuts import render

from . import forms
from .models import Order, OrderLineItem


def checkout(request):
    """A view to display checkout page """

    form = forms.OrderForm

    context = {
        'form': form,
    }
    return render(request, 'checkout/checkout.html', context)