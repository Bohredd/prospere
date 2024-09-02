from django.contrib import admin
from core.models import Arquivo, Solicitacao, Tag, Interesse, RequisitoOportunidade

admin.site.register(Arquivo)
admin.site.register(Solicitacao)
admin.site.register(Tag)
admin.site.register(Interesse)
admin.site.register(RequisitoOportunidade)
