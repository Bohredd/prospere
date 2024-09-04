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
    texto = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        # Se o objeto já existir, não faz a leitura e a atualização do texto
        if not self.pk:
            super(Arquivo, self).save(*args, **kwargs)

        if self.is_texto():
            # Use a instância existente para evitar duplicações
            # Lê o arquivo e atualiza o campo texto
            with self.file.open('r') as file:
                self.texto = file.read()

            # Atualiza o objeto no banco de dados sem criar uma nova entrada
            super(Arquivo, self).save(update_fields=['texto'])
    def is_texto(self):

        exts_text_showable = [
            'txt',
            'doc',
            'docx',
            'py',
            'md',
        ]

        ext = self.file.name.split('.')[-1]

        return ext in exts_text_showable

    def is_image(self):

        exts_image_showable = [
            'png',
            'jpg',
            'jpeg',
            'gif',
        ]

        ext = self.file.name.split('.')[-1]

        return ext in exts_image_showable

    def is_pdf(self):

        exts_pdf_showable = [
            'pdf',
        ]

        ext = self.file.name.split('.')[-1]

        return ext in exts_pdf_showable

    def get_texto(self):
        if self.is_texto():
            return self.texto
        return None
class RespostaRequisito(models.Model):
    requisito = models.ForeignKey('core.Requisito', on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)
    arquivos = models.ManyToManyField(Arquivo, blank=True, related_name='respostas_requisitos')
    foto = models.ImageField(null=True, blank=True)
    links = models.URLField(null=True, blank=True)
    checkbox = models.BooleanField(default=False, null=True, blank=True)
    respondido_por = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    respondido_empresa = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Resposta de Requisito'
        verbose_name_plural = 'Respostas de Requisitos'

class Interesse(models.Model):
    vaga = models.ForeignKey('oportunidades.Oportunidade', on_delete=models.CASCADE)
    resposta_requisitos = models.ForeignKey('core.RespostaRequisito', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

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