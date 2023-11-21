from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),  # index url
    path("about/", views.about, name="about"),  # about url
    path("contact/", views.contact, name="contact"),  # contact url
    path("prediction/", views.prediction, name="prediction"),  # prediction url
]
