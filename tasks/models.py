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
    snoozed_till = models.DateTimeField(null=True, blank=True, default=None)

    def is_completed(self):
        return bool(self.completed_at)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def json_script_id(self):
        return f"task-json-{self.id}"

    def __str__(self):
        return self.title
