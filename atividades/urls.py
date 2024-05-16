from django.contrib import admin
from django.urls import path
from atividades.views import AtividadeListCreate, AtividadeRetrieveUpdateDestroy

urlpatterns = [
    path('', AtividadeListCreate.as_view(), name='atividade-list-create'),
    path('/<int:pk>/', AtividadeRetrieveUpdateDestroy.as_view(), name='atividade-retrieve-update-destroy'),
]
