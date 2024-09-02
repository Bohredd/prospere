from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.estado.nome}"

class Universidade(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class AreaAtuacao(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome