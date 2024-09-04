from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200, unique=True, help_text="Nome da empresa")
    cnpj = models.CharField(max_length=18, unique=True, help_text="CNPJ da empresa")
    endereco = models.CharField(max_length=300, blank=True, null=True, help_text="Endereço da empresa")
    telefone = models.CharField(max_length=15, blank=True, null=True, help_text="Telefone de contato")
    email = models.EmailField(max_length=254, blank=True, null=True, help_text="Email de contato")
    site = models.URLField(max_length=200, blank=True, null=True, help_text="Site da empresa")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome
