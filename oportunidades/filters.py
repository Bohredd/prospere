# oportunidades/filters.py

import django_filters
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.widgets import CheckboxInput
from oportunidades.models import Oportunidade
from universidades.models import Cidade, Universidade, Curso, AreaAtuacao
from oportunidades.constants import TipoOportunidade, TipoTrabalho

class OportunidadeFilter(django_filters.FilterSet):
    cidade = django_filters.ModelChoiceFilter(
        queryset=Cidade.objects.all(),
        empty_label="Todos",
        label = 'Cidades: '
    )
    universidade = django_filters.ModelChoiceFilter(
        queryset=Universidade.objects.all(),
        empty_label="Todas",
        label = 'Universidades: '
    )
    cursos = django_filters.ModelMultipleChoiceFilter(
        queryset=Curso.objects.all(),
        widget=CheckboxSelectMultiple,
        conjoined=False,
        label='Cursos Relacionados',
    )
    areas_atuacao = django_filters.ModelMultipleChoiceFilter(
        queryset=AreaAtuacao.objects.all(),
        widget=CheckboxSelectMultiple,  # Use CheckboxSelectMultiple do Django
        label='Áreas de Atuação',
    )
    tipo = django_filters.ChoiceFilter(
        choices=TipoOportunidade.choices,
        empty_label="Todos",
        label='Tipo de Oportunidade:',
    )
    tipo_trabalho = django_filters.ChoiceFilter(
        choices=TipoTrabalho.choices,
        empty_label="Todos",
        label = 'Tipo de Trabalho:',
    )
    is_remunerado = django_filters.BooleanFilter(
        field_name='is_remunerado',
        label='Com remuneração?',
        widget=CheckboxInput,
    )

    class Meta:
        model = Oportunidade
        fields = [
            'cidade',
            'universidade',
            'cursos',
            'areas_atuacao',
            'tipo',
            'tipo_trabalho',
            'is_remunerado',
        ]