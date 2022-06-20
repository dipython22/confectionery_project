# Generated by Django 4.0.3 on 2022-06-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0006_alter_cake_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email_name',
            field=models.EmailField(default='@', max_length=250, verbose_name='el.paštas'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'patvirtintas'), ('g', 'gaminamas'), ('a', 'paruoštas atsiemimui')], db_index=True, default='p', max_length=1, verbose_name='užsakymo būsena'),
        ),
    ]