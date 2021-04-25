from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from . import forms
from .models import Order, OrderLineItem


def checkout(request):
    """A view to display checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request,
                       "There is nothing in your basket, please add an item")
        return redirect(reverse('deals'))

    form = forms.OrderForm

    context = {
        'form': form,
    }
    return render(request, 'checkout/checkout.html', context)
