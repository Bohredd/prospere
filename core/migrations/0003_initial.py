# Generated by Django 5.1 on 2024-09-04 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='respostarequisito',
            name='respondido_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interesse',
            name='resposta_requisitos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.respostarequisito'),
        ),
    ]
