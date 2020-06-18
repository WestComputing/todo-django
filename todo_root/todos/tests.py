from datetime import timedelta

from django.test import TestCase
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


class TodoModelTest(TestCase):
    def setUp(self):
        self.todos = []
        for index, task in enumerate(SAMPLE_TASKS):
            self.todos.append(Todo.objects.create(
                task=task,
                completed=not bool((index + 1) % 3),
                # created=timezone.now(),
                due=timezone.now() + timedelta(days=index - 2)
            ))

    def test_01_create_todos(self):
        for todo in self.todos:
            query = Todo.objects.get(task=todo.task)
            self.assertEqual(query, todo)
