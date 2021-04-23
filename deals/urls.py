from django.urls import path
from . import views

urlpatterns = [
    path('deals', views.deals, name='deals')
]
