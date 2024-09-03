from django.db import models

class Requisito(models.Model):

    precisa_texto = models.BooleanField(default=False)
    precisa_arquivos = models.BooleanField(default=False)
    precisa_foto = models.BooleanField(default=False)
    precisa_links = models.BooleanField(default=False)
    precisa_checkbox = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'

