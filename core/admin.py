from django.contrib import admin
from core.models import Requisito, RespostaRequisito, Interesse, Arquivo, RespostaInteresse

admin.site.register(Requisito)
admin.site.register(RespostaRequisito)
admin.site.register(Interesse)
admin.site.register(RespostaInteresse)
admin.site.register(Arquivo)