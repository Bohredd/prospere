# Generated by Django 5.1 on 2024-09-04 18:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_arquivo_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesse',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
