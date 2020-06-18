from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    pass


class DetailView(generic.DetailView):
    pass


class NewFormView(generic.FormView):
    pass


class EditFormView(generic.FormView):
    pass


class DeleteFormView(generic.FormView):
    pass
