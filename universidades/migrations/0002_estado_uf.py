# Generated by Django 5.1 on 2024-09-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universidades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='uf',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
