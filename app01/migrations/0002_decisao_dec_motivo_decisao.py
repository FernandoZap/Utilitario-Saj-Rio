# Generated by Django 4.1 on 2022-09-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decisao_dec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipodecisao', models.IntegerField()),
                ('id_decisao', models.IntegerField()),
                ('descricao', models.CharField(max_length=200)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Motivo_Decisao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipodecisao', models.IntegerField()),
                ('id_decisao', models.IntegerField()),
                ('id_motivo', models.IntegerField()),
                ('descricao', models.CharField(max_length=200)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
    ]
