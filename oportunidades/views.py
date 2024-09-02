from django.views.generic import ListView, DetailView
from .models import Oportunidade
from core.forms import TagFilterForm

class OportunidadeListView(ListView):
    """View para listar todas as oportunidades com filtro de tags."""

    model = Oportunidade
    template_name = "oportunidades/oportunidades_lista.html"
    context_object_name = "oportunidades"

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TagFilterForm(self.request.GET or None)

        if form.is_valid():
            tipo_tag = form.cleaned_data.get('tipo_tag')
            if tipo_tag:
                queryset = queryset.filter(tags__tipo_tag=tipo_tag).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TagFilterForm(self.request.GET or None)
        return context

class OportunidadeDetailView(DetailView):
    """View para detalhar a oportunidade."""
    model = Oportunidade
    template_name = 'oportunidades/oportunidade_detalhes.html'
    context_object_name = 'oportunidade'

    def get_object(self):
        return super().get_object()