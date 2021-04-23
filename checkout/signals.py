from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def updateOnSave(sender, instance, created, **kwargs):
    """
    update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def updateOnSave(sender, instance, created, **kwargs):
    """
    update order total on lineitem delete
    """
    instance.order.update_total()