from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from core.models import RequisitoOportunidade
from oportunidades.models import Oportunidade
from eventos.models import Evento
from .forms import RequisitoOportunidadeForm
from .models import Solicitacao

class RequisitoOportunidadeFormView(FormView):
    template_name = 'core/gerar_solicitacao.html'
    form_class = RequisitoOportunidadeForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tipo_solicitacao = self.kwargs.get('tipo_solicitacao')
        requisito_id = self.kwargs.get('requisito_id')

        if tipo_solicitacao == '1':  # Oportunidade
            oportunidade = get_object_or_404(Oportunidade, pk=requisito_id)
            requisito = oportunidade.requisito
        elif tipo_solicitacao == '2':  # Evento
            evento = get_object_or_404(Evento, pk=requisito_id)
            requisito = evento.requisito
        else:
            raise ValueError("Tipo de solicitação inválido")

        kwargs['tipo_solicitacao'] = tipo_solicitacao
        kwargs['requisito'] = requisito
        return kwargs

    def form_valid(self, form):
        solicitacao = form.save(commit=False)
        tipo_solicitacao = self.kwargs.get('tipo_solicitacao')

        if tipo_solicitacao == '1':  # Oportunidade
            oportunidade = get_object_or_404(Oportunidade, pk=self.kwargs.get('requisito_id'))
            solicitacao.oportunidade = oportunidade
        elif tipo_solicitacao == '2':  # Evento
            evento = get_object_or_404(Evento, pk=self.kwargs.get('requisito_id'))
            solicitacao.evento = evento

        solicitacao.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('success_url')
