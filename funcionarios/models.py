from django.db import models
from setores.models import Setor


class Funcionario(models.Model):
    nome = models.CharField("Nome", max_length=255)
    sobrenome = models.CharField("Sobrenome", max_length=255)
    email = models.EmailField("Endereço de email", unique=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, related_name="setor", null=True, default=None)

    def __str__(self):
        return self.nome
