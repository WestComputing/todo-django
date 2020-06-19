from datetime import timedelta

from django.utils import timezone

if __name__ == '__main__':
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
        title=task.upper(),
        description=task,
        completed=not bool((index + 1) % 3),
        due=timezone.now() + timedelta(days=index - 2),
    ))
