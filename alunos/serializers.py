from rest_framework import serializers
from .models import aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = aluno
        fields = '__all__'
