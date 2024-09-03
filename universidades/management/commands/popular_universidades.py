from django.core.management.base import BaseCommand
from universidades.models import Estado, Cidade, Universidade, Curso, AreaAtuacao
class Command(BaseCommand):
    help = 'Popula os cursos da Universidade Federal de Santa Maria em cada cidade'

    def handle(self, *args, **kwargs):
        # Criar ou obter o estado do Rio Grande do Sul
        estado_rs, created = Estado.objects.get_or_create(nome='Rio Grande do Sul', uf='RS')

        campus = [
            'Santa Maria',
            'Cachoeira do Sul',
            'Frederico Westphalen',
            'Palmeira das Missões',
            'Estudo a Distância',
        ]

        # Dicionário de cidades e cursos
        cidades_cursos = {
            'Santa Maria': [
                'ABI - Artes Cênicas',
                'ABI - Ciências Biológicas',
                'Administração',
                'Agronegócio',
                'Agronomia',
                'Alimentos',
                'Arquitetura e Urbanismo',
                'Arquivologia',
                'Artes Cênicas - Direção Teatral',
                'Artes Cênicas - Interpretação Teatral',
                'Artes Visuais',
                'Ciência da Computação',
                'Ciências Biológicas',
                'Ciências Contábeis',
                'Ciências Econômicas',
                'Ciências Sociais',
                'Comunicação Social - Produção Editorial',
                'Comunicação Social - Publicidade e Propaganda',
                'Comunicação Social - Relações Públicas',
                'Dança - Bacharelado',
                'Dança - Licenciatura',
                'Desenho Industrial',
                'Direito',
                'Educação Especial',
                'Educação Especial Inclusiva',
                'Educação Física',
                'Eletrônica Industrial',
                'Enfermagem',
                'Engenharia Acústica',
                'Engenharia Aeroespacial',
                'Engenharia Ambiental e Sanitária',
                'Engenharia Civil',
                'Engenharia Elétrica',
                'Engenharia Florestal',
                'Engenharia Mecânica',
                'Engenharia Química',
                'Engenharia da Computação',
                'Engenharia de Controle e Automação',
                'Engenharia de Produção',
                'Engenharia de Telecomunicações',
                'Estatística',
                'Fabricação Mecânica',
                'Farmácia',
                'Filosofia',
                'Fisioterapia',
                'Fonoaudiologia',
                'Física',
                'Geografia',
                'Geoprocessamento',
                'Gestão Ambiental',
                'Gestão de Cooperativas',
                'Gestão de Turismo',
                'História',
                'Jornalismo',
                'Letras - Espanhol',
                'Letras - Inglês',
                'Letras - Língua Portuguesa',
                'Letras - Português',
                'Matemática',
                'Mbya Guarani Educação Intercultural Indígena',
                'Medicina',
                'Medicina Veterinária',
                'Meteorologia',
                'Música',
                'Música e Tecnologia',
                'Nutrição',
                'Não Consta',
                'Odontologia',
                'Pedagogia',
                'Processos Químicos',
                'Programa Especial de Graduação de Formação de Professores para A Educação Profissional',
                'Psicologia',
                'Química',
                'Química Industrial',
                'Redes de Computadores',
                'Relações Internacionais',
                'Serviço Social',
                'Sistemas de Informação',
                'Sistemas para Internet',
                'Teatro',
                'Terapia Ocupacional',
                'Zootecnia',
            ],
            'Cachoeira do Sul': [
                'Arquitetura e Urbanismo',
                'Engenharia Agrícola',
                'Engenharia Elétrica',
                'Engenharia Mecânica',
                'Engenharia de Transportes e Logística',
            ],
            'Frederico Westphalen': [
                'Agronomia',
                'Direito',
                'Engenharia Ambiental e Sanitária',
                'Engenharia Florestal',
                'Jornalismo',
                'Licenciatura Intercultural Indígena',
                'Relações Públicas',
                'Sistemas de Informação',
            ],
            'Palmeira das Missões': [
                'Administração',
                'Ciências Biológicas',
                'Ciências Econômicas',
                'Enfermagem',
                'Nutrição',
                'Zootecnia',
            ],
            'Educação a Distância': [
                'Ciências da Religião',
                'Computação',
                'Educação Especial',
                'Educação Indígena',
                'Educação do Campo',
                'Física',
                'Geografia',
                'Letras - Espanhol',
                'Letras - Português',
                'Pedagogia',
                'Programa Especial de Graduação de Formação de Professores para A Educação Profissional',
                'Sociologia',
            ],
        }

        # Áreas de atuação
        areas_atuacao_dict = {
            'Tecnologia': [
                'Ciência da Computação',
                'Engenharia da Computação',
                'Sistemas de Informação',
                'Redes de Computadores',
                'Computação',
            ],
            'Saúde': [
                'Medicina',
                'Enfermagem',
                'Fisioterapia',
                'Nutrição',
                'Odontologia',
                'Medicina Veterinária',
            ],
            'Educação': [
                'Pedagogia',
                'Educação Física',
                'Educação Especial',
                'Educação do Campo',
                'Educação Especial Inclusiva',
                'Letras - Espanhol',
                'Letras - Português',
                'Ciências da Religião',
                'Educação Indígena',
                'Programa Especial de Graduação de Formação de Professores para A Educação Profissional',
                'Licenciatura Intercultural Indígena',
                'Mbya Guarani Educação Intercultural Indígena',
            ],
            'Humanas': [
                'Direito',
                'Comunicação Social - Produção Editorial',
                'Comunicação Social - Publicidade e Propaganda',
                'Comunicação Social - Relações Públicas',
                'Psicologia',
                'Serviço Social',
                'História',
                'Filosofia',
                'Sociologia',
                'Ciências Sociais',
                'Geografia',
                'Relações Internacionais',
                'Jornalismo',
                'Artes Cênicas',
                'Artes Visuais',
                'Dança - Bacharelado',
                'Dança - Licenciatura',
                'Teatro',
                'Arquivologia',
                'Biblioteconomia',
            ],
            'Exatas': [
                'Matemática',
                'Estatística',
                'Física',
                'Química',
                'Química Industrial',
                'Geoprocessamento',
                'Engenharia Ambiental e Sanitária',
                'Engenharia Civil',
                'Engenharia Elétrica',
                'Engenharia Florestal',
                'Engenharia Mecânica',
                'Engenharia Química',
                'Engenharia da Computação',
                'Engenharia de Controle e Automação',
                'Engenharia de Produção',
                'Engenharia de Telecomunicações',
                'Desenho Industrial',
                'Fabricação Mecânica',
                'Processos Químicos',
                'Geoprocessamento',
            ],
        }

        # Criar ou obter áreas de atuação
        areas_atuacao = {}
        for area_nome in areas_atuacao_dict.keys():
            area, created = AreaAtuacao.objects.get_or_create(nome=area_nome)
            areas_atuacao[area_nome] = area

        # Iterar sobre as cidades e cursos
        for cidade_nome, cursos in cidades_cursos.items():
            cidade, created = Cidade.objects.get_or_create(nome=cidade_nome, estado=estado_rs)
            universidade, created = Universidade.objects.get_or_create(nome='Universidade Federal de Santa Maria', cidade=cidade)

            for curso_nome in cursos:
                curso, created = Curso.objects.get_or_create(nome=curso_nome, universidade=universidade)

                # Associar áreas de atuação ao curso
                for area_nome, cursos_areas in areas_atuacao_dict.items():
                    if curso_nome in cursos_areas:
                        curso.areas_atuacao.add(areas_atuacao[area_nome])

        self.stdout.write(self.style.SUCCESS('Cursos criados com sucesso!'))
