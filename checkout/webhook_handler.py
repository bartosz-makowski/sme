from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Order, OrderLineItem
from deals.models import Deal

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle a  webhook event payment_intent.succeeded"""
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details

        order_exists = False
        attempt = 1
        while attempt <= 5:
            print('15000')
            try:
                print('2000')
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number=billing_details.phone,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    town_or_city__iexact=billing_details.address.city,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                print('order doesnotexist')
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in the database', status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    town_or_city=billing_details.address.city,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Deal.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    print('dupa')
                    order.delete()
                else:
                    print('ichuj')
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}', status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in the database',
            status=200)

    def handle_payment_intent_failed(self, event):
        """Handle a  webhook event payment_intent.failed"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
