# Generated by Django 3.2.13 on 2023-06-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Digimon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre del digimon.', max_length=128)),
                ('img', models.CharField(help_text='Ingrese una imagen por favor.', max_length=256)),
                ('level', models.CharField(help_text='Ingrese el nivel por favor.', max_length=128)),
            ],
        ),
    ]
