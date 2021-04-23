from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date')
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem)
