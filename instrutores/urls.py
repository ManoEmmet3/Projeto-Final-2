from django.urls import path
from .views import InstrutorListCreate, ContactRetrieveUpdateDestroy

urlpatterns = [
    path('', InstrutorListCreate.as_view(), name='adicionar_instrutor'),
    path('/<int:pk>/', ContactRetrieveUpdateDestroy.as_view(), name='instrutor-detail'),
]

