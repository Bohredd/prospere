from django.db import models

# Create your models here.

class Estado(models.Model):

    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.nome


class Cidade(models.Model):

    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome

class Curso(models.Model):

    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nome

class Universidade(models.Model):

    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Universidade"
        verbose_name_plural = "Universidades"

    def __str__(self):
        return self.nome