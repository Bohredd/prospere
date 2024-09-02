from django.db import models
from core.constants import TipoSolicitacao


class Solicitacao(models.Model):
    tipo = models.CharField(max_length=100, choices=TipoSolicitacao.choices, default="")
    respondida = models.BooleanField(default=False)
    texto = models.TextField(null=True, blank=True)
    usuario_enviante = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    oportunidade_referente = models.ForeignKey(
        "oportunidades.Oportunidade", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"

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
