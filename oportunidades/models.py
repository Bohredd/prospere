from django.db import models
from oportunidades.constants import TipoOportunidade, TipoTrabalho

class Oportunidade(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=100,
        choices=TipoOportunidade.choices,
        default="",
    )
    ativo = models.BooleanField(default=True)
    descricao = models.TextField(null=True, blank=True)
    numero_contato = models.CharField(max_length=100, null=True, blank=True)
    email_contato = models.EmailField(null=True, blank=True)
    quantia_vagas = models.IntegerField(default=0, null=True, blank=True)
    is_remunerado = models.BooleanField(default=False)
    remuneracao = models.FloatField(default=0, null=True, blank=True)
    tipo_trabalho = models.CharField(max_length=100, choices=TipoTrabalho.choices, default='')
    tags = models.ManyToManyField('core.Tag', blank=True)
    areas = models.ManyToManyField('oportunidades.Area', blank=True)
    cursos = models.ManyToManyField('universidades.Curso', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    requisito = models.ForeignKey('core.RequisitoOportunidade', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Oportunidade"
        verbose_name_plural = "Oportunidades"

    def __str__(self):
        return self.nome

class Area(models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    requisitos = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.nome
