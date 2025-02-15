import os
import django
import random
from faker import Faker

# Configurar o Django para rodar o script externamente
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from funcionarios.models import Funcionario
from setores.models import Setor

fake = Faker("pt_BR")


setores_nomes = ["TI", "Contabilidade", "Financeiro", "Atendimento", "Orçamento"]


setores = {}
for nome in setores_nomes:
    setor, created = Setor.objects.get_or_create(nome=nome)
    setores[nome] = setor


quantidade_funcionarios = 50  # Altere conforme necessário

for _ in range(quantidade_funcionarios):
    nome = fake.first_name()
    sobrenome = fake.last_name()
    email = fake.email()
    setor = random.choice(list(setores.values()))

    Funcionario.objects.create(
        nome=nome,
        sobrenome=sobrenome,
        email=email,
        setor=setor
    )

print("Funcionários e setores populados com sucesso!")