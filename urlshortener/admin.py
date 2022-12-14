from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ("long_url", "short_url", "created_at")
    readonly_fields = ("short_url", "created_at")
