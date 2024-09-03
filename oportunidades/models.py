from django.db import models
from oportunidades.constants import TipoOportunidade, TipoTrabalho

class Oportunidade(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(
        max_length=3,
        choices=TipoOportunidade.choices,
        default='',
    )
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    is_remunerado = models.BooleanField(default=False)
    remuneracao = models.FloatField(default=0.0)
    quantia = models.IntegerField(default=1)
    universidade = models.ForeignKey('universidades.Universidade', on_delete=models.CASCADE, null=True, blank=True)
    cursos = models.ManyToManyField('universidades.Curso', blank=True)
    areas_atuacao = models.ManyToManyField('universidades.AreaAtuacao', blank=True)
    cidade = models.ForeignKey('universidades.Cidade', on_delete=models.CASCADE, null=True, blank=True)
    estado = models.ForeignKey('universidades.Estado', on_delete=models.CASCADE, null=True, blank=True)
    tipo_trabalho = models.CharField(
        max_length=2,
        choices=TipoTrabalho.choices,
        default=TipoTrabalho.PRESENCIAL,
    )
    requisitos_envio = models.ForeignKey(
        'core.Requisito',
        on_delete=models.CASCADE,
    )
    requisitos_oportunidade = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    beneficios_oportunidade = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Oportunidade'
        verbose_name_plural = 'Oportunidades'

    def __str__(self):
        return self.titulo