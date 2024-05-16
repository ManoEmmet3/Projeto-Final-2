from rest_framework import serializers
from .models import Atividade
from instrutores.models import Instrutor

class AtividadeSerializer(serializers.ModelSerializer):
    instrutores = serializers.PrimaryKeyRelatedField(queryset=Instrutor.objects.all(), many=True)

    class Meta:
        model = Atividade
        fields = '__all__'

    def create(self, validated_data):
        instrutores_data = validated_data.pop('instrutores')
        atividade = Atividade.objects.create(**validated_data)
        atividade.instrutores.set(instrutores_data)
        return atividade

    def update(self, instance, validated_data):
        instrutores_data = validated_data.pop('instrutores', None)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.data = validated_data.get('data', instance.data)
        instance.hora_inicio = validated_data.get('hora_inicio', instance.hora_inicio)
        instance.hora_fim = validated_data.get('hora_fim', instance.hora_fim)
        instance.capacidade_maxima = validated_data.get('capacidade_maxima', instance.capacidade_maxima)
        instance.local = validated_data.get('local', instance.local)
        instance.save()

        if instrutores_data is not None:
            instance.instrutores.set(instrutores_data)

        return instance
