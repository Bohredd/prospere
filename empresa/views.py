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
        context['respostas'] = RespostaRequisito.objects.filter(interesse=interesse)
        if self.request.method == 'POST':
            form = RespostaInteresseForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                resposta = form.save(commit=False)
                resposta.interesse = interesse
                resposta.respondido_por = self.request.user
                resposta.save()
                return redirect('detalhe_respostas', pk=interesse.pk)
        else:
            form = RespostaInteresseForm()
        context['form'] = form
        return context

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
        )