from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f"{self.nome} - {self.estado.nome}"

class Universidade(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Universidade'
        verbose_name_plural = 'Universidades'

    def __str__(self):
        return self.nome + ' - ' + self.cidade.nome + ' - ' + self.cidade.estado.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    areas_atuacao = models.ManyToManyField(
        'AreaAtuacao',
        related_name='areas_atuacao_curso',
    )
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome + ' - ' + self.universidade.cidade.nome

class AreaAtuacao(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Área de Atuação'
        verbose_name_plural = 'Áreas de Atuação'

    def __str__(self):
        return self.nome