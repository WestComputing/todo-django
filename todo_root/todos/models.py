from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now)
    due = models.DateField(null=True, default=timezone.now() + timedelta(days=7))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def due_today(self):
        return bool(self.due == timezone.localdate())

    def overdue(self):
        return bool(self.due < timezone.localdate())

    def __str__(self):
        return f"{self.id}: {self.title} " \
               f"created: {self.created.strftime('%Y-%m-%d')} " \
               f"due: {self.due.strftime('%Y-%m-%d')} " \
               f"{'complete' if self.completed else 'incomplete'}"
