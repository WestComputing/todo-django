from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin

from .models import Todo


class UserMatchesTodo(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().user


class FormStampUser(ModelFormMixin):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.filter(user_id=self.request.user.id).order_by('due')


class ItemView(LoginRequiredMixin, UserMatchesTodo, DetailView):
    model = Todo


class NewFormView(LoginRequiredMixin, CreateView, FormStampUser):
    model = Todo
    fields = ['title', 'description', 'completed', 'due']
    success_url = reverse_lazy('todos:index')


class EditFormView(LoginRequiredMixin, UserMatchesTodo, UpdateView, FormStampUser):
    model = Todo
    fields = ['title', 'description', 'completed', 'created', 'due']
    template_name_suffix = '_edit_form'

    def get_success_url(self):
        return reverse('todos:detail', kwargs={'pk': self.object.pk})


class DeleteFormView(LoginRequiredMixin, UserMatchesTodo, DeleteView):
    model = Todo
    success_url = reverse_lazy('todos:index')
