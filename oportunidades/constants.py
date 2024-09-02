from django.db import models

class TipoOportunidade(models.TextChoices):

    estagio = 'estagio', 'Estágio'
    trabalho = 'trabalho', 'Trabalho'
    voluntario = 'voluntario', 'Voluntário'