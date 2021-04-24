from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from deals.models import Deal


def basket(request):
    """A view to display basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, deal_id):

    deal = Deal.objects.get(pk=deal_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if deal_id in list(basket.keys()):
        basket[deal_id] += quantity
    else:
        basket[deal_id] = quantity
        messages.success(request, f'Added {deal.name} to your bag')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, deal_id):

    basket = request.session.get('basket', {})
    basket.pop(deal_id)

    request.session['basket'] = basket
    return redirect(reverse('basket'))
