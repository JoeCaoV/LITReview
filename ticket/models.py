from django.db import models
from django.conf import settings


class Ticket(models.Model):
    title = models.CharField(
        max_length=128,
    )

    description = models.TextField(
        max_length=128,
        blank=True,
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    time_created = models.DateTimeField(
        auto_now_add=True,
    )
