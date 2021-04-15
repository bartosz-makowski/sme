from django.urls import path
from . import views

urlpatterns = [
    path('location', views.location, name='location')
]
