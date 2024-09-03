# Generated by Django 5.1 on 2024-09-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oportunidades', '0002_oportunidade_beneficios_oportunidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oportunidade',
            name='tipo',
            field=models.CharField(choices=[('EST', 'Estágio'), ('VAG', 'Vaga'), ('VOL', 'Voluntariado'), ('BOL', 'Bolsa')], default='', max_length=3),
        ),
    ]
