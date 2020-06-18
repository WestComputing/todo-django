from datetime import timedelta

from django.utils import timezone

from .models import Todo

SAMPLE_TASKS = [
    "First thing we do is...",
    "Second",
    "Third time's a charm",
    "Fourth be with you",
    "Fifth Element",
    "Sixth Sense",
    "The Seventh Guest"
]

todos = []
for index, task in enumerate(SAMPLE_TASKS):
    todos.append(Todo.objects.create(
        task=task,
        completed=not bool((index + 1) % 3),
        # created=timezone.now(),
        due=timezone.now() + timedelta(days=index - 2),
    ))
