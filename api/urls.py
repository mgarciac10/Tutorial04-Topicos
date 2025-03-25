from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.ToDoListCreate.as_view(), name='list'),
    path('todos/<int:pk>', views.ToDoRetrieveUpdateDestroy.as_view())
]