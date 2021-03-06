# Generated by Django 4.0.3 on 2022-06-26 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tortukai', '0006_alter_cake_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CakeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField(verbose_name='atsiliepimas')),
                ('cake', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cake_reviews', to='tortukai.cake', verbose_name='tortas')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cake_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Klientas')),
            ],
        ),
    ]
