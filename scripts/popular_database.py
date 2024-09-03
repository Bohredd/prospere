import os
import django
import sys
from django.core.management import call_command
from django.contrib.auth import get_user_model
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prospere.settings')
django.setup()
call_command('makemigrations')

call_command('migrate')

User = get_user_model()

superuser_email = 'admin@bohredd.dev'
superuser_nomecompleto = 'diogo'
superuser_password = 'diogo2012'

if not User.objects.filter(email=superuser_email).exists():
    User.objects.create_superuser(
        nome_completo=superuser_nomecompleto,
        email=superuser_email,
        password=superuser_password
    )
    print(f'Superusuário "{superuser_email}" criado com sucesso!')
else:
    print(f'O superusuário "{superuser_email}" já existe!')

call_command('popular_universidades')
call_command('popular_oportunidades')