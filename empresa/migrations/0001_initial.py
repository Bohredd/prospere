# Generated by Django 5.1 on 2024-09-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da empresa', max_length=200, unique=True)),
                ('cnpj', models.CharField(help_text='CNPJ da empresa', max_length=18, unique=True)),
                ('endereco', models.CharField(blank=True, help_text='Endereço da empresa', max_length=300, null=True)),
                ('telefone', models.CharField(blank=True, help_text='Telefone de contato', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, help_text='Email de contato', max_length=254, null=True)),
                ('site', models.URLField(blank=True, help_text='Site da empresa', null=True)),
            ],
        ),
    ]
