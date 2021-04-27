from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from . import forms
from .models import Order, OrderLineItem
from basket.contexts import basket_contents

import stripe


def checkout(request):
    """A view to display checkout page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request,
                       "There is nothing in your basket, please add an item")
        return redirect(reverse('deals'))

    form = forms.OrderForm
    current_basket = basket_contents(request)
    total = current_basket['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripepublic key is missing. \
            Please add this information')

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)
