from rest_framework import generics
from .models import Atividade
from .serializers import AtividadeSerializer

class AtividadeListCreate(generics.ListCreateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

class AtividadeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
