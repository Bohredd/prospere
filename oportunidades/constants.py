from django.db import models

class TipoOportunidade(models.TextChoices):
    ESTAGIO = 'EST', 'Estágio'
    TRABALHO = 'TRA', 'Trabalho'
    VOLUNTARIADO = 'VOL', 'Voluntariado'

class TipoTrabalho(models.TextChoices):
    HOME_OFFICE = 'HO', 'Home Office'
    PRESENCIAL = 'PR', 'Presencial'
    HIBRIDO = 'HI', 'Híbrido'