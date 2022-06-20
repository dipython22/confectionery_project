# Generated by Django 4.0.3 on 2022-06-19 19:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0002_client_alter_occasion_options_alter_occasion_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(max_length=156, verbose_name='torto pavadinimas')),
                ('cake_description', models.TextField(default='nėra duomenų', max_length=1000, verbose_name='karamelinis su riešutais')),
                ('occasion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='tortukai.occasion', verbose_name='torto pavadinimas')),
            ],
            options={
                'verbose_name': 'tortuko pavadinimas',
                'verbose_name_plural': 'tortukų pavadinimai',
                'ordering': ['cake_name'],
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='email_name',
            field=models.EmailField(max_length=250, verbose_name='el.paštas'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.IntegerField(default=370, max_length=11, verbose_name='tel.nr.:'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='užsakymo numeris')),
                ('notice', models.CharField(default='', max_length=500, null=True, verbose_name='pastabos')),
                ('deadline', models.DateField(blank=True, db_index=True, verbose_name='pagaminti datai: ')),
                ('status', models.CharField(blank=True, choices=[('up', 'užsakymas patvirtintas'), ('g', 'gaminama'), ('pa', 'paruoštas atsiemimui')], db_index=True, default='ok', max_length=2, verbose_name='prieinamumas')),
                ('cake', models.ManyToManyField(related_name='orders', to='tortukai.cake', verbose_name='tortas')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='tortukai.client', verbose_name='klientas')),
            ],
            options={
                'verbose_name': 'spec. priemonės vienetas',
                'verbose_name_plural': 'spec. priemonių atsargos',
            },
        ),
    ]