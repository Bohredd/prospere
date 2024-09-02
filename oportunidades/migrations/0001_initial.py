# Generated by Django 5.1 on 2024-09-02 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oportunidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('EST', 'Estágio'), ('TRA', 'Trabalho'), ('VOL', 'Voluntariado')], default='EST', max_length=3)),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('is_remunerado', models.BooleanField(default=False)),
                ('remuneracao', models.FloatField(default=0.0)),
                ('quantia', models.IntegerField(default=1)),
                ('tipo_trabalho', models.CharField(choices=[('HO', 'Home Office'), ('PR', 'Presencial'), ('HI', 'Híbrido')], default='PR', max_length=2)),
                ('areas_atuacao', models.ManyToManyField(blank=True, to='universidades.areaatuacao')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universidades.cidade')),
                ('cursos', models.ManyToManyField(blank=True, to='universidades.curso')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universidades.estado')),
                ('universidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universidades.universidade')),
            ],
            options={
                'verbose_name': 'Oportunidade',
                'verbose_name_plural': 'Oportunidades',
            },
        ),
    ]
