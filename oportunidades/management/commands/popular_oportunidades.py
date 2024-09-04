from django.core.management.base import BaseCommand
from oportunidades.models import Oportunidade
from universidades.models import Universidade, Curso, AreaAtuacao, Cidade, Estado
from core.models import Requisito
from empresa.models import Empresa  # Certifique-se de que o caminho está correto para o modelo Empresa
from oportunidades.constants import TipoOportunidade, TipoTrabalho

class Command(BaseCommand):
    help = 'Popula o banco de dados com algumas oportunidades, requisitos e empresas'

    def handle(self, *args, **kwargs):
        # Criar alguns requisitos
        requisito1, _ = Requisito.objects.get_or_create(
            precisa_texto=True,
            precisa_arquivos=True,
            precisa_foto=False,
            precisa_links=False,
            precisa_checkbox=False,
            helptext_texto="Texto necessário para envio.",
            helptext_arquivos="Arquivos necessários para envio.",
            helptext_foto="Foto não necessária.",
            helptext_links="Links não necessários.",
            helptext_checkbox="Checkbox não necessário."
        )

        requisito2, _ = Requisito.objects.get_or_create(
            precisa_texto=False,
            precisa_arquivos=True,
            precisa_foto=True,
            precisa_links=True,
            precisa_checkbox=True,
            helptext_texto="Texto não necessário.",
            helptext_arquivos="Arquivos necessários para envio.",
            helptext_foto="Foto necessária.",
            helptext_links="Links necessários.",
            helptext_checkbox="Checkbox necessário."
        )

        # Criar algumas empresas
        empresa1, _ = Empresa.objects.get_or_create(
            nome='Tech Solutions Ltda',
            cnpj='12.345.678/0001-90',
            endereco='Rua das Tecnologias, 123',
            telefone='11 98765-4321',
            email='contato@techsolutions.com.br',
            site='http://www.techsolutions.com.br'
        )

        empresa2, _ = Empresa.objects.get_or_create(
            nome='Data Analysts Inc.',
            cnpj='98.765.432/0001-01',
            endereco='Avenida dos Dados, 456',
            telefone='11 91234-5678',
            email='info@dataanalysts.com.br',
            site='http://www.dataanalysts.com.br'
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
                'quantia_horas_semanais': 20,
                'quantia_horas_dia': 4,
                'quantia_horas_intervalo_dia': 1,
                'universidade': universidade,
                'cursos': [curso_engenharia],
                'areas_atuacao': [area_tecnologia],
                'cidade': cidade_sao_paulo,
                'estado': estado,
                'tipo_trabalho': TipoTrabalho.PRESENCIAL,
                'requisitos_envio': requisito1,
                'requisitos_oportunidade': 'Conhecimentos em HTML, CSS e JavaScript.',
                'beneficios_oportunidade': 'Vale transporte e auxílio alimentação.',
                'empresa': empresa1,
            },
            {
                'titulo': 'Analista de Dados Sênior',
                'descricao': 'Vaga para analista de dados com ampla experiência em análise de grandes volumes de dados.',
                'tipo': TipoOportunidade.VAGA,
                'is_remunerado': True,
                'remuneracao': 8000.0,
                'quantia': 1,
                'quantia_horas_semanais': 40,
                'quantia_horas_dia': 8,
                'quantia_horas_intervalo_dia': 1,
                'universidade': universidade,
                'cursos': [curso_engenharia],
                'areas_atuacao': [area_tecnologia],
                'cidade': cidade_sao_paulo,
                'estado': estado,
                'tipo_trabalho': TipoTrabalho.HIBRIDO,
                'requisitos_envio': requisito2,
                'requisitos_oportunidade': 'Experiência com Python e SQL.',
                'beneficios_oportunidade': 'Plano de saúde e bônus anual.',
                'empresa': empresa2,
            },
            {
                'titulo': 'Voluntário em Projetos de Tecnologia',
                'descricao': 'Oportunidade de voluntariado em projetos de tecnologia para ajudar em iniciativas sociais.',
                'tipo': TipoOportunidade.VOLUNTARIADO,
                'is_remunerado': False,
                'quantia': 1,
                'quantia_horas_semanais': 10,
                'quantia_horas_dia': 2,
                'quantia_horas_intervalo_dia': 0,
                'universidade': universidade,
                'cursos': [],
                'areas_atuacao': [area_tecnologia],
                'cidade': cidade_sao_paulo,
                'estado': estado,
                'tipo_trabalho': TipoTrabalho.PRESENCIAL,
                'requisitos_envio': requisito1,
                'requisitos_oportunidade': 'Desejo de colaborar em projetos sociais.',
                'beneficios_oportunidade': 'Certificado de participação e networking.',
                'empresa': empresa1,
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
                    'quantia_horas_semanais': opp_data.get('quantia_horas_semanais', 0),
                    'quantia_horas_dia': opp_data.get('quantia_horas_dia', 0),
                    'quantia_horas_intervalo_dia': opp_data.get('quantia_horas_intervalo_dia', 0),
                    'universidade': opp_data.get('universidade'),
                    'cidade': opp_data.get('cidade'),
                    'estado': opp_data.get('estado'),
                    'tipo_trabalho': opp_data.get('tipo_trabalho', TipoTrabalho.PRESENCIAL),
                    'requisitos_envio': opp_data.get('requisitos_envio'),
                    'requisitos_oportunidade': opp_data.get('requisitos_oportunidade', ''),
                    'beneficios_oportunidade': opp_data.get('beneficios_oportunidade', ''),
                    'empresa': opp_data.get('empresa'),
                }
            )
            # Adicionar cursos e áreas de atuação, se não estiverem presentes
            if created:
                oportunidade.cursos.set(opp_data.get('cursos', []))
                oportunidade.areas_atuacao.set(opp_data.get('areas_atuacao', []))
                oportunidade.save()

        self.stdout.write(self.style.SUCCESS('Oportunidades, requisitos e empresas criados com sucesso!'))
