from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('write-review', views.write_review, name='write-review'),
]
