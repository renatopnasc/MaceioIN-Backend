# Generated by Django 5.1.6 on 2025-02-12 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_alter_funcionario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={},
        ),
        migrations.AlterModelManagers(
            name='funcionario',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='first_name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='last_name',
            new_name='sobrenome',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='password',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='username',
        ),
    ]
