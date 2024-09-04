from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django_filters.views import FilterView
from .models import Oportunidade
from .filters import OportunidadeFilter
from .forms import InteresseForm
from core.models import Requisito, RespostaRequisito, Interesse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class OportunidadeListView(FilterView, ListView):
    model = Oportunidade
    template_name = 'oportunidades/lista.html'
    context_object_name = 'oportunidades'
    filterset_class = OportunidadeFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        # Adicione lógica adicional para o queryset, se necessário
        return queryset

class OportunidadeDetailView(DetailView):
    model = Oportunidade
    template_name = 'oportunidades/detalhes.html'
    context_object_name = 'oportunidade'

class InteresseFormView(FormView):
    template_name = 'oportunidades/interesse_form.html'  # Nome do template onde o formulário será exibido
    form_class = InteresseForm
    success_url = reverse_lazy('listar_oportunidades')  # URL para redirecionar após o sucesso

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pk = self.kwargs.get('pk')
        requisito = get_object_or_404(Requisito, pk=pk)  # Obtém o objeto com base no 'pk'
        kwargs['requisito'] = requisito
        return kwargs

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('login')

        # Obter o objeto Requisito
        pk = self.kwargs.get('pk')
        requisito = get_object_or_404(Requisito, pk=pk)

        arquivos = self.request.FILES.getlist('arquivos')

        # Criar a resposta do requisito
        resposta_requisito = RespostaRequisito.objects.create(
            requisito=requisito,
            texto=form.cleaned_data.get('texto'),
            foto=form.cleaned_data.get('foto'),
            links=form.cleaned_data.get('links'),
            checkbox=form.cleaned_data.get('checkbox'),
            respondido_por=self.request.user  # Usuário autenticado
        )

        for arquivo in arquivos:
            resposta_requisito.arquivos.create(file=arquivo)

        resposta_requisito.save()

        # Criar o interesse
        oportunidade_id = self.kwargs.get('pk')

        oportunidade = get_object_or_404(Oportunidade, id=oportunidade_id)

        interesse = Interesse.objects.create(
            vaga=oportunidade,
            resposta_requisitos=resposta_requisito
        )
        interesse.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        # Aqui você pode tratar o caso em que o formulário é inválido
        return super().form_invalid(form)