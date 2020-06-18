from datetime import timedelta

from django.db import models
from django.utils import timezone


class Todo(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    due = models.DateTimeField(null=True, default=timezone.now() + timedelta(days=7))

    def __str__(self):
        return f"Task {self.id}: {self.task[:20]} " \
               f"created: {self.created.strftime('%Y-%m-%d')} " \
               f"due: {self.due.strftime('%Y-%m-%d')} " \
               f"{'complete' if self.completed else 'incomplete'}"
