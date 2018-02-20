# Generated by Django 2.0.2 on 2018-02-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('publicacao', models.DateField(blank=True, null=True, verbose_name='Publicacao')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('criado_em', models.DateTimeField(verbose_name='Criado em')),
            ],
        ),
    ]
