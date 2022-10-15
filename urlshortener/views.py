import re
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Url
from .forms import UrlForm


def index(request): 
    if request.method == "POST":
        url_form = UrlForm(request.POST)
        if url_form.is_valid():
            url_obj = url_form.save()
            url = f"{request.scheme}://{request.get_host()}/{url_obj.short_url}"
            return render(request, "urlshortener/index.html", {"form": url_form, "url": url})
    else:
        url_form = UrlForm()
    return render(request, "urlshortener/index.html", {"form": url_form})


def redirect_url(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    return redirect(url.long_url)


def view_404(request, exception=None):
    return redirect(reverse("home_page"))
