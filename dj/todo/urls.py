from django.urls import path
from todo import views

urlpatterns = [
    path('', views.TaskList, name='tasks'),
    path('<str:pk>', views.TaskDelete, name="delete"),
]