from django.db import models


class TipoSolicitacao(models.TextChoices):

    estagio = "estagio", "Estágio"
    trabalho = "trabalho", "Trabalho"
    evento = "evento", "Evento"
    voluntario = "voluntario", "Voluntário"


class TipoTag(models.TextChoices):

    por_curso = 'por_curso', 'Por Curso'
    por_cidade = 'por_cidade', 'Por Cidade'
    por_universidade = 'por_universidade', 'Por Universidade'
    por_area = 'por_area', 'Por Area'
    por_tipo_trabalho = 'por_tipo_trabalho', 'Por Trabalho'
    por_tipo_oportunidade = 'por_tipo_oportunidade', 'Por Oportunidade'
    por_evento = 'por_evento', 'Por Evento'