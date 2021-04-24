from django.shortcuts import get_object_or_404
from deals.models import Deal


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Deal, pk=item_id)
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count
    }

    return context
