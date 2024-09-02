from django.db import models
from core.constants import TipoSolicitacao, TipoTag


class Solicitacao(models.Model):
    tipo = models.CharField(max_length=100, choices=TipoSolicitacao.choices, default="")
    respondida = models.BooleanField(default=False)
    texto = models.TextField(null=True, blank=True)
    usuario_enviante = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    oportunidade_referente = models.ForeignKey(
        "oportunidades.Oportunidade", on_delete=models.CASCADE
    )
    evento_referente = models.ForeignKey("eventos.Evento", on_delete=models.CASCADE)

    # campos do requisitos da oportunidade ou evento
    curriculo = models.FileField(upload_to='curriculos/', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    email_contato = models.EmailField(null=True, blank=True)
    telefone_contato = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"

    def update_interessados(self):
        if self.tipo in ['estagio', 'trabalho', 'voluntariado']:
            oportunidade_referente = self.oportunidade_referente
            oportunidade_referente.quantia_interessados += 1
            oportunidade_referente.save()
        else:
            evento = Evento.objects.get(pk=self.evento_referente.pk)
            evento.quantia_interessados += 1
            evento.save()

    def __str__(self):
        return f"Solicitação {self.tipo} - {'Respondida' if self.respondida else 'Não Respondida'}"


class Arquivo(models.Model):
    solicitacao = models.ForeignKey(
        Solicitacao, related_name="arquivos", on_delete=models.CASCADE
    )
    arquivo = models.FileField(upload_to="arquivos/")

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"

    def __str__(self):
        return f"Arquivo {self.arquivo.name}"

class Tag(models.Model):
    """

    Usado para filtrar as oportunidades e/ou eventos

    """
    nome = models.CharField(max_length=100)
    tipo_tag = models.CharField(max_length=100, choices=TipoTag.choices, default='')
    nome_relacionado = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nome

class Interesse(models.Model):

    is_oportunidade = models.BooleanField(default=False)
    oportunidade = models.ForeignKey(
        'oportunidades.Oportunidade', on_delete=models.CASCADE
    )

    is_evento = models.BooleanField(default=False)
    evento = models.ForeignKey(
        'eventos.Evento', on_delete=models.CASCADE
    )

    quantia_interessados = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"

    def __str__(self):
        return f"{self.oportunidade.nome} - {self.quantia_interessados} interessados" if self.is_oportunidade else f"{self.evento.nome} - {self.quantia_interessados} interessados"

class RequisitoOportunidade(models.Model):
    precisa_curriculo = models.BooleanField(default=False)
    precisa_descricao = models.BooleanField(default=False)
    precisa_email_contato = models.BooleanField(default=False)
    precisa_telefone_contato = models.BooleanField(default=False)
    precisa_endereco = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Requisito Oportunidade'
        verbose_name_plural = 'Requisitos das Oportunidades'
