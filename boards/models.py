from django.db import models
from django.urls import reverse
from django.utils import timezone


class Board(models.Model):
    slug = models.CharField(max_length=30, unique=True)
    ip = models.GenericIPAddressField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("boards:view", kwargs={"slug": self.slug})
