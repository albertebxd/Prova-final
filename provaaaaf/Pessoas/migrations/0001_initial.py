# Generated by Django 4.0.6 on 2022-07-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('idade', models.CharField(max_length=2)),
                ('departamento', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
    ]
