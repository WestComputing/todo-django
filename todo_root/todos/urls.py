from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.NewFormView.as_view(), name='new'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.EditFormView.as_view(), name='edit'),
    path('<int:pk>/delete', views.DeleteFormView.as_view(), name='delete'),
]
