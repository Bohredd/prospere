from django.db import models

class TipoOportunidade(models.TextChoices):
    ESTAGIO = 'EST', 'Estágio'
    VAGA = 'VAG', 'Vaga'
    VOLUNTARIADO = 'VOL', 'Voluntariado'
    BOLSA = 'BOL', 'Bolsa'

class TipoTrabalho(models.TextChoices):
    HOME_OFFICE = 'HO', 'Home Office'
    PRESENCIAL = 'PR', 'Presencial'
    HIBRIDO = 'HI', 'Híbrido'