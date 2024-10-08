from __future__ import annotations
from django.contrib.auth.models import AbstractUser
from django.db import models
from usuarios.managers import UsuarioManager

class Usuario(AbstractUser):
    username = None
    first_name = None
    last_name = None
    nome_completo = models.CharField(
        "Nome Completo", max_length=100, blank=False, null=False
    )
    email = models.EmailField("E-mail", blank=True, unique=True)
    cpf = models.CharField(max_length=14, unique=True, null=True)  # 123.456.789-09
    telefone = models.CharField(max_length=11, blank=True, null=True)  # (11) 98765-4321
    data_nascimento = models.DateField("Data de  Nascimento", blank=True, null=True)
    imagem = models.ImageField(blank=True, null=True,upload_to="usuarios/images")
    pertence_empresa = models.BooleanField(default=False)
    pertence_universidade = models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)
    empresa_vinculada = models.ForeignKey(
        'empresa.Empresa', on_delete=models.CASCADE, blank=True, null=True
    )
    universidade_vinculada = models.ForeignKey(
        'universidades.Universidade', on_delete=models.CASCADE, blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome_completo"]

    objects = UsuarioManager()

    def __str__(self):
        return self.nome_completo

    def get_primeiro_nome(self):
        return self.nome_completo.split(" ")[0]