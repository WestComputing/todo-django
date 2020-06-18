from django.urls import path

from .views import IndexView, NewFormView, ItemView, EditFormView, DeleteFormView

app_name = 'todos'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new/', NewFormView.as_view(), name='new'),
    path('<int:pk>/', ItemView.as_view(), name='detail'),
    path('<int:pk>/edit', EditFormView.as_view(), name='edit'),
    path('<int:pk>/delete', DeleteFormView.as_view(), name='delete'),
]
