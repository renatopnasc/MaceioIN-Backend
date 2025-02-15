from django.db import models

class Setor(models.Model):
    nome = models.CharField("Nome do setor", max_length=255)

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

    def __str__(self):
        return self.nome