from django.urls import path
from .views import alunoListCreate, alunoRetrieveUpdateDestroy

urlpatterns = [
    path('', alunoListCreate.as_view(), name='adicionar_alunos'),
    path('/<int:pk>/', alunoRetrieveUpdateDestroy.as_view(), name='instrutor-detail'),
]

