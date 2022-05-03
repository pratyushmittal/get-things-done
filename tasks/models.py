from django.db import models
from django.utils import timezone

from boards.models import Board


class Category(models.Model):
    name = models.CharField(max_length=50)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title
