# Generated by Django 5.1 on 2024-09-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_respostarequisito_respondido_empresa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
