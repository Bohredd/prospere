from django.db import models

class TipoOportunidade(models.TextChoices):

    estagio = 'estagio', 'Estágio'
    trabalho = 'trabalho', 'Trabalho'
    voluntario = 'voluntario', 'Voluntário'

class TipoTrabalho(models.TextChoices):

    home_office = 'home_office', 'Home Office'
    presencial = 'presencial', 'Presencial'
    hibrido = 'hibrido', 'Hibrido'