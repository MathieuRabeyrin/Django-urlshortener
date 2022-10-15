from operator import index
from django.urls import path
from .views import index, redirect_url


urlpatterns = [
    path("", index, name="home_page"),
    path("<str:short_url>", redirect_url, name="redirect_url")
]