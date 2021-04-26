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
        'stripe_public_key': 'pk_test_51IkGcQCqi9X9Ek55OpYF0Joe1pb0BVQHR2KyAAeK9OwUUETzm97MTTtl9gTnC8efj0TeckiXCpfEWRkurUKyZAR900Zvlos3DT',
        'client_secret': 'test client secret',
    }
    return render(request, 'checkout/checkout.html', context)
