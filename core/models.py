from django.db import models

class Requisito(models.Model):
    precisa_texto = models.BooleanField(default=False)
    helptext_texto = models.CharField(max_length=200, null=True, blank=True)
    precisa_arquivos = models.BooleanField(default=False)
    helptext_arquivos = models.CharField(max_length=200, null=True, blank=True)
    precisa_foto = models.BooleanField(default=False)
    helptext_foto = models.CharField(max_length=200, null=True, blank=True)
    precisa_links = models.BooleanField(default=False)
    helptext_links = models.CharField(max_length=200, null=True, blank=True)
    precisa_checkbox = models.BooleanField(default=False)
    helptext_checkbox = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'

class Arquivo(models.Model):
    file = models.FileField(upload_to='respostas_arquivos/')

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return self.file.name

class RespostaRequisito(models.Model):
    requisito = models.ForeignKey('core.Requisito', on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)
    arquivos = models.ManyToManyField(Arquivo, blank=True, related_name='respostas_requisitos')
    foto = models.ImageField(null=True, blank=True)
    links = models.URLField(null=True, blank=True)
    checkbox = models.BooleanField(default=False, null=True, blank=True)
    respondido_por = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Resposta de Requisito'
        verbose_name_plural = 'Respostas de Requisitos'

class Interesse(models.Model):
    vaga = models.ForeignKey('oportunidades.Oportunidade', on_delete=models.CASCADE)
    resposta_requisitos = models.ForeignKey('core.RespostaRequisito', on_delete=models.CASCADE)

    def get_respondido_por(self):
        return self.resposta_requisitos.respondido_por

class RespostaInteresse(models.Model):

    interesse = models.ForeignKey('core.Interesse', on_delete=models.CASCADE)
    respondido_por = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)
    aprovado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Resposta de Interesse'
        verbose_name_plural = 'Respostas de Interesses'