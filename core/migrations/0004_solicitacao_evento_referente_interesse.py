# Generated by Django 5.1 on 2024-09-02 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tag'),
        ('eventos', '0002_evento_tags'),
        ('oportunidades', '0002_area_oportunidade_cursos_oportunidade_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='evento_referente',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eventos.evento'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_oportunidade', models.BooleanField(default=False)),
                ('is_evento', models.BooleanField(default=False)),
                ('quantia_interessados', models.IntegerField(default=0)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
                ('oportunidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oportunidades.oportunidade')),
            ],
            options={
                'verbose_name': 'Interesse',
                'verbose_name_plural': 'Interesses',
            },
        ),
    ]
