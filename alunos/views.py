from django.urls import reverse
from rest_framework import generics
from .models import aluno
from .serializers import AlunoSerializer
from rest_framework.response import Response




class alunoListCreate(generics.ListCreateAPIView):
    queryset = aluno.objects.all()
    serializer_class = AlunoSerializer

class alunoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = aluno.objects.all()
    serializer_class = AlunoSerializer