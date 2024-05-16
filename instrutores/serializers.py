from django.forms import ValidationError
from rest_framework import serializers
from .models import Instrutor

    
from rest_framework import serializers

class InstrutorSerializer(serializers.ModelSerializer):
    # validar o telefone
    telefone = serializers.RegexField(
        regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
        error_messages={'invalid': 'Formato de telefone inválido. Use o formato (XX) XXXX-XXXX.'}
    )
  
    def validate_cref(self, value):
        
        if len(value) != 9 or value[6] != '/':
            raise serializers.ValidationError("O formato do CREF deve ser: 'XXXXXX/XX'")
        if not value[:4].isdigit():
            raise serializers.ValidationError("Os quatro primeiros caracteres do CREF devem ser números.")
        if not value[4:6].isalpha() or not value[7:].isalpha():
            raise serializers.ValidationError("Os dois últimos caracteres antes e depois da barra devem ser letras.")
        return value
    
    class Meta:
        model = Instrutor
        fields = '__all__'

    
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor
        fields = '__all__'