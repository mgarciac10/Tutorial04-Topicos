from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from todo.models import ToDo

# Create your views here.

class ToDoListCreate(generics.ListCreateAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and 
    # queryset. 
    # We specify TodoSerializer which we have earlier implemented 
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ToDoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts 
        return ToDo.objects.filter(user=user)