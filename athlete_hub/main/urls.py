
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("triathlon", views.triathlon, name = "triathlon"),
]