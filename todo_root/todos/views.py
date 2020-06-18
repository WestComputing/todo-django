from django.shortcuts import render
from django.views import generic
from .models import Todo


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.all()


class DetailView(generic.DetailView):
    pass


class NewFormView(generic.FormView):
    pass


class EditFormView(generic.FormView):
    pass


class DeleteFormView(generic.FormView):
    pass
