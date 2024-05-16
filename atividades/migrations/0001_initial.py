# Generated by Django 4.1.3 on 2024-05-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instrutores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fim', models.TimeField()),
                ('capacidade_maxima', models.PositiveIntegerField()),
                ('instrutores', models.ManyToManyField(to='instrutores.instrutor')),
            ],
        ),
    ]
