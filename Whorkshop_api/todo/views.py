from django.shortcuts import render
from rest_framework import viewsets
from .models import TodoList, Pessoa
from .serializers import TodoListSerializer, PessoaSerializer
# Create your views here.

class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class PessoaViewset(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
