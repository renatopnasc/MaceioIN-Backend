from rest_framework import serializers
from .models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    setor = serializers.StringRelatedField()

    class Meta:
        model = Funcionario
        fields = ['nome', "sobrenome", "email", "setor"]