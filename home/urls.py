from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),  # index url
    path("about", views.about, name="about"),  # about url
]
