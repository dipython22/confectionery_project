# Generated by Django 4.0.4 on 2022-06-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0021_orderline_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='price_per_item',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kaina už vnt.'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='summ_per_line',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Suma'),
        ),
    ]