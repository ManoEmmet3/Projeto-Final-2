
from urllib import response
from django.urls import reverse
from rest_framework import generics
from .models import Instrutor
from .serializers import InstrutorSerializer , ContactSerializer

class InstrutorListCreate(generics.ListCreateAPIView):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer

class ContactRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrutor.objects.all()
    serializer_class = ContactSerializer
    
  