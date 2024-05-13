from django.urls import path
from . import views

urlpatterns = [
    path("log_in", views.log_in, name="log_in"),
    path("sing_in", views.sing_in, name="sing_in"),
    path("BookKO", views.home_page2, name="home_page2"),
]
