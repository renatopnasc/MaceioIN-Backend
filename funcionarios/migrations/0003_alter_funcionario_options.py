# Generated by Django 5.1.6 on 2025-02-12 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_alter_funcionario_setor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
    ]
