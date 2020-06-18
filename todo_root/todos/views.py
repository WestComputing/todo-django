from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Todo


class IndexView(ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.all().order_by('due')


class ItemView(DetailView):
    model = Todo


class NewFormView(CreateView):
    model = Todo
    fields = ['title', 'description', 'completed', 'due']
    success_url = reverse_lazy('todos:index')


class EditFormView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed', 'created', 'due']
    template_name_suffix = '_edit_form'

    def get_success_url(self):
        return reverse('todos:detail', kwargs={'pk': self.object.pk})


class DeleteFormView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos:index')
