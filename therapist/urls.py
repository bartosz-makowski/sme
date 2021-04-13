from django.urls import path
from . import views

urlpatterns = [
    path('therapist', views.therapist, name='therapist')
]