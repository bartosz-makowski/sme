from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from . import forms
from .forms import OrderForm
from .models import Order, OrderLineItem
from deals.models import Deal
from basket.contexts import basket_contents

import stripe


def checkout(request):
    """A view to display checkout page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method ==  'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
        }

        form = OrderForm(form_data)

        if form.is_valid():
            order = form.save()
            for item_id, item_data in basket.items():
                try:
                    deal = Deal.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            deal=deal,
                            quantity=item_data
                    )
                    order_line_item.save()
                except Deal.DoesNotExists:
                    messages.error(request,
                                   "One of the items in your basket wasn't found in our database. Please contact us for help"
                                   )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request,
                           'There was an error with your form. Please try again')
    else:
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


def checkout_success(request, order_number):
    """Handles successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(reqeust, f'Order successful! \
        Your order number is {order_number}. A confirmation email will be sent to {order.email}. We will be in touch to arrange your appointment')
    if 'basket' in request.session:
        del request.session['basket']
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(reqeust, template, context)