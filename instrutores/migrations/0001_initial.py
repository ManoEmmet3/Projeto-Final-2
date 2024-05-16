# Generated by Django 4.1.3 on 2024-05-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cref', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=11, unique=True)),
            ],
        ),
    ]
