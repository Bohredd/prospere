# Generated by Django 5.1 on 2024-09-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_solicitacao_evento_referente_interesse'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequisitoOportunidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precisa_curriculo', models.BooleanField(default=False)),
                ('precisa_descricao', models.BooleanField(default=False)),
                ('precisa_email_contato', models.BooleanField(default=False)),
                ('precisa_telefone_contato', models.BooleanField(default=False)),
                ('precisa_endereco', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Requisito Oportunidade',
                'verbose_name_plural': 'Requisitos das Oportunidades',
            },
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='curriculo',
            field=models.FileField(blank=True, null=True, upload_to='curriculos/'),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='email_contato',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='endereco',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='telefone_contato',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
