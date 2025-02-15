# MaceióIN Backend

Este é um projeto básico utilizando Django. Abaixo estão as instruções para configurar e iniciar o ambiente de desenvolvimento.

## Pré-requisitos

- Python 3.8+ instalado
- pip (gerenciador de pacotes do Python)
- Git (para clonar o repositório)

## Configuração do Ambiente de Desenvolvimento

### 1. Clone o repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

### 2. Criação do Ambiente Virtual

```bash
python3 -m venv venv
```

### 3. Ative a venv

```bash
source venv/bin/activate
```

### 4. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 5. Criar um Superusuário
```bash
python manage.py createsuperuser
```

### 6. Iniciar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

Isso iniciará o servidor no endereço padrão http://127.0.0.1:8000/. Você pode acessar o painel administrativo em: http://127.0.0.1:8000/admin/
