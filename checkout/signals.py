from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

def updateOnSave(sender, instance, created, **kwargs):
    """
    update order total
    """