from django.core.management.base import BaseCommand
from oportunidades.models import Oportunidade
from universidades.models import Universidade, Curso, AreaAtuacao, Cidade, Estado
from core.models import Requisito  # Certifique-se de que o caminho está correto para o modelo Requisito
from oportunidades.constants import TipoOportunidade, TipoTrabalho

class Command(BaseCommand):
    help = 'Popula o banco de dados com algumas oportunidades e requisitos'

    def handle(self, *args, **kwargs):
        # Criar alguns requisitos
        requisito1, _ = Requisito.objects.get_or_create(
            precisa_texto=True,
            precisa_arquivos=True,
            precisa_foto=False,
            precisa_links=False,
            precisa_checkbox=False
        )

        requisito2, _ = Requisito.objects.get_or_create(
            precisa_texto=False,
            precisa_arquivos=True,
            precisa_foto=True,
            precisa_links=True,
            precisa_checkbox=True
        )

        # Obter ou criar instâncias necessárias para as oportunidades
        estado, _ = Estado.objects.get_or_create(nome='São Paulo', uf='SP')
        cidade_sao_paulo, _ = Cidade.objects.get_or_create(nome='São Paulo', estado=estado)
        universidade, _ = Universidade.objects.get_or_create(nome='Universidade de São Paulo', cidade=cidade_sao_paulo)
        curso_engenharia, _ = Curso.objects.get_or_create(nome='Engenharia de Computação', universidade=universidade)
        area_tecnologia, _ = AreaAtuacao.objects.get_or_create(nome='Tecnologia')

        # Criar algumas oportunidades
        oportunidades = [
            {
                'titulo': 'Estágio em Desenvolvimento de Software',
                'descricao': 'Oportunidade para estágio em desenvolvimento de software, com foco em tecnologias web.',
                'tipo': TipoOportunidade.ESTAGIO,
                'is_remunerado': True,
                'remuneracao': 1500.0,
                'quantia': 1,
                'universidade': universidade,
                'cursos': [curso_engenharia],
                'areas_atuacao': [area_tecnologia],
                'cidade': cidade_sao_paulo,
                'estado': estado,
                'tipo_trabalho': TipoTrabalho.PRESENCIAL,
                'requisitos_envio': requisito1,
                'requisitos_oportunidade': 'Conhecimentos em HTML, CSS e JavaScript.',
                'beneficios_oportunidade': 'Vale transporte e auxílio alimentação.',
            },
            {
                'titulo': 'Analista de Dados Sênior',
                'descricao': 'Vaga para analista de dados com ampla experiência em análise de grandes volumes de dados.',
                'tipo': TipoOportunidade.VAGA,
                'is_remunerado': True,
                'remuneracao': 8000.0,
                'quantia': 1,
                'universidade': universidade,
                'cursos': [curso_engenharia],
                'areas_atuacao': [area_tecnologia],
                'cidade': cidade_sao_paulo,
                'estado': estado,
                'tipo_trabalho': TipoTrabalho.HIBRIDO,
                'requisitos_envio': requisito2,
                'requisitos_oportunidade': 'Experiência com Python e SQL.',
                'beneficios_oportunidade': 'Plano de saúde e bônus anual.',
            },
            {
                'titulo': 'Voluntário em Projetos de Tecnologia',
                'descricao': 'Oportunidade de voluntariado em projetos de tecnologia para ajudar em iniciativas sociais.',
                'tipo': TipoOportunidade.VOLUNTARIADO,
                'is_remunerado': False,
                'quantia': 1,
                'universidade': universidade,
                'cursos': [],
                'areas_atuacao': [area_tecnologia],
                'cidade': cidade_sao_paulo,
                'estado': estado,
                'tipo_trabalho': TipoTrabalho.PRESENCIAL,
                'requisitos_envio': requisito1,
                'requisitos_oportunidade': 'Desejo de colaborar em projetos sociais.',
                'beneficios_oportunidade': 'Certificado de participação e networking.',
            },
        ]

        # Inserir as oportunidades no banco de dados
        for opp_data in oportunidades:
            oportunidade, created = Oportunidade.objects.get_or_create(
                titulo=opp_data['titulo'],
                defaults={
                    'descricao': opp_data['descricao'],
                    'tipo': opp_data['tipo'],
                    'is_remunerado': opp_data.get('is_remunerado', False),
                    'remuneracao': opp_data.get('remuneracao', 0.0),
                    'quantia': opp_data.get('quantia', 1),
                    'universidade': opp_data.get('universidade'),
                    'cidade': opp_data.get('cidade'),
                    'estado': opp_data.get('estado'),
                    'tipo_trabalho': opp_data.get('tipo_trabalho', TipoTrabalho.PRESENCIAL),
                    'requisitos_envio': opp_data.get('requisitos_envio'),
                    'requisitos_oportunidade': opp_data.get('requisitos_oportunidade', ''),
                    'beneficios_oportunidade': opp_data.get('beneficios_oportunidade', ''),
                }
            )
            # Adicionar cursos e áreas de atuação, se não estiverem presentes
            if created:
                oportunidade.cursos.set(opp_data.get('cursos', []))
                oportunidade.areas_atuacao.set(opp_data.get('areas_atuacao', []))
                oportunidade.save()

        self.stdout.write(self.style.SUCCESS('Oportunidades e requisitos criados com sucesso!'))
