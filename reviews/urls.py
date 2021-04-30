from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('write_review/', views.write_review, name='write_review'),
]
