from django.db import models


class TipoSolicitacao(models.TextChoices):

    estagio = "estagio", "Estágio"
    trabalho = "trabalho", "Trabalho"
    evento = "evento", "Evento"
    voluntario = "voluntario", "Voluntário"
