from django.db import models


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)
    local = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    is_pago = models.BooleanField(default=False)
    valor_entrada = models.FloatField(null=True, blank=True)
    tags = models.ManyToManyField('core.Tag', blank=True)
    requisito = models.ForeignKey('core.RequisitoOportunidade', on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return f"{self.nome} ({self.data_inicio.strftime('%d/%m/%Y')})"
