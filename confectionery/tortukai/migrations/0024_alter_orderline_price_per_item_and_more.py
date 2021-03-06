# Generated by Django 4.0.4 on 2022-06-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0023_alter_orderline_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='price_per_item',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Kaina už vnt.'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='kiekis'),
        ),
    ]
