from django.urls import path
from . import views

urlpatterns = [
    path('basket', views.basket, name='basket'),
    path('add/<deal_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<deal_id>/', views.adjust_basket, name='adjust_basket'),
]
