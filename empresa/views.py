from django.views.generic import DetailView, ListView, FormView
from django.shortcuts import get_object_or_404, render, redirect
from core.models import Interesse, RespostaRequisito, RespostaInteresse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RespostaInteresseForm

class DetalheRespostasView(LoginRequiredMixin, DetailView):
    model = Interesse
    template_name = 'empresa/detalhe_respostas.html'
    context_object_name = 'interesse'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interesse = self.get_object()
        context['resposta'] = RespostaRequisito.objects.filter(interesse=interesse, respondido_empresa=False).first()
        context['form'] = RespostaInteresseForm()
        return context

    def post(self, request, *args, **kwargs):
        interesse = self.get_object()
        form = RespostaInteresseForm(request.POST, request.FILES)
        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.interesse = interesse
            resposta.respondido_por = self.request.user
            resposta.save()
            resposta_requisito_pk = form.cleaned_data.get('resposta_requisito_pk')
            if resposta_requisito_pk:
                try:
                    resposta_requisito = RespostaRequisito.objects.get(pk=resposta_requisito_pk)
                    resposta_requisito.respondido_empresa = True
                    resposta_requisito.save()
                except RespostaRequisito.DoesNotExist:
                    pass  # Trate o caso conforme necessário
            return redirect('detalhe_respostas', pk=interesse.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ListaInteressesView(LoginRequiredMixin, ListView):
    model = Interesse
    template_name = 'empresa/lista_interesses.html'
    context_object_name = 'interesses'

    def get_queryset(self):
        # Verifica se o usuário é uma empresa
        if not self.request.user.pertence_empresa:
            return Interesse.objects.none()  # Retorna uma queryset vazia

        return Interesse.objects.filter(
            vaga__empresa=self.request.user.empresa_vinculada,
            resposta_requisitos__respondido_empresa=False,
        ).order_by(
            '-criado_em'
        )