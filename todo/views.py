from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import TodoItem

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoItem.objects.all()

#provides the implementation of crud operations
#specifies serialiser_class and queryset
