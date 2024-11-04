from django.urls import path
from presentation.views import index, ContactView, apropos, temoignage, service

urlpatterns = [
    path("", index, name="index"),
    path("service/", service, name="service"),
    path("temoignage/", temoignage, name="temoignage"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("apropos/", apropos, name="about"),
]