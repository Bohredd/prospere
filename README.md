<h1>Plataforma de Oportunidades e Eventos da UFSM - Prospere</h1>

<p>Bem-vindo à <strong>Prospere</strong>, a plataforma de oportunidades e eventos da Universidade Federal de Santa Maria (UFSM). Esta plataforma foi desenvolvida para facilitar o acesso dos alunos às oportunidades de vagas de emprego, estágios e eventos acadêmicos, permitindo também o envio de candidaturas diretamente pela plataforma.</p>

<h2>Funcionalidades Principais</h2>

<h3>1. <strong>Exploração de Oportunidades</strong></h3>
<ul>
    <li>Navegue por uma lista de vagas de emprego, estágios, bolsas de estudo e outras oportunidades disponíveis.</li>
    <li>Cada oportunidade inclui detalhes como descrição da vaga, número de vagas, requisitos, contato e informações adicionais.</li>
</ul>

<h3>2. <strong>Eventos Acadêmicos e Profissionais</strong></h3>
<ul>
    <li>Acesse uma seção dedicada a eventos, como palestras, workshops, seminários e conferências.</li>
    <li>Visualize informações como data, local, descrição e oportunidades de participação em eventos acadêmicos e profissionais.</li>
</ul>

<h3>3. <strong>Candidatura a Vagas</strong></h3>
<ul>
    <li>Manifeste interesse em vagas diretamente pela plataforma.</li>
    <li>Envie seu currículo e outras informações relevantes durante o processo de candidatura.</li>
    <li>Receba notificações por e-mail quando for selecionado ou quando a vaga exigir alguma ação adicional.</li>
</ul>

<h3>4. <strong>Gerenciamento de Perfis</strong></h3>
<ul>
    <li>Crie e gerencie seu perfil na plataforma, incluindo informações pessoais, histórico acadêmico, experiência profissional e habilidades.</li>
    <li>Atualize seu currículo a qualquer momento para refletir as informações mais recentes.</li>
</ul>

<h2>Tecnologias Utilizadas</h2>
<ul>
    <li><strong>Back-end:</strong> Django (Python)</li>
    <li><strong>Front-end:</strong> HTML, CSS, JavaScript, HTMX</li>
    <li><strong>Banco de Dados:</strong> PostgreSQL</li>
    <li><strong>Autenticação:</strong> Django Authentication com suporte a integração via OAuth2</li>
    <li><strong>Notificações:</strong> Sistema de envio de e-mails (SMTP)</li>
</ul>

<h2>Requisitos de Instalação</h2>
<p>Certifique-se de ter os seguintes requisitos instalados:</p>
<ul>
    <li>Python 3.8+</li>
    <li>Django 4.x</li>
    <li>PostgreSQL</li>
    <li>Git</li>
</ul>

<h3>Passos para Instalação</h3>
<ol>
    <li>Clone o repositório do projeto:
        <pre><code>git clone https://github.com/Bohredd/prospere.git
cd prospere</code></pre>
    </li>
    <li>Crie um ambiente virtual e instale as dependências:
        <pre><code>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt</code></pre>
    </li>
    <li>Configure o banco de dados no arquivo <code>settings.py</code>:
        <pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}</code></pre>
    </li>
    <li>Execute as migrações para configurar o banco de dados:
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li>Crie um superusuário para acessar o painel administrativo:
        <pre><code>python manage.py createsuperuser</code></pre>
    </li>
    <li>Inicie o servidor de desenvolvimento:
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>Acesse a aplicação em <a href="http://localhost:8000">http://localhost:8000</a>.</li>
</ol>

<h2>Contribuição</h2>
<p>Se você deseja contribuir para o projeto, siga estas etapas:</p>
<ol>
    <li>Faça um fork do repositório.</li>
    <li>Crie uma branch para sua funcionalidade (<code>git checkout -b minha-nova-funcionalidade</code>).</li>
    <li>Faça o commit de suas alterações (<code>git commit -m 'Adiciona nova funcionalidade'</code>).</li>
    <li>Envie para o repositório remoto (<code>git push origin minha-nova-funcionalidade</code>).</li>
    <li>Abra um Pull Request.</li>
</ol>

<h2>Licença</h2>
<p>Este projeto está licenciado sob a <a href="LICENSE">Licença MIT</a>.</p>

<h2>Contato</h2>
<p>Para mais informações ou para relatar problemas, entre em contato com a equipe de desenvolvimento pelo e-mail: <a href="mailto:suporte@ufsm.br">suporte@ufsm.br</a>.</p>
