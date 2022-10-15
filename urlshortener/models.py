from django.db import models
from django.utils.timezone import now
from nanoid import generate


def create_id():
    return generate(size=8)


class Url(models.Model):
    long_url = models.URLField(max_length=255)
    short_url = models.CharField(default=create_id, max_length=8, editable=False)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.short_url