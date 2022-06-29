# Generated by Django 4.0.3 on 2022-06-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0030_alter_orderline_price_per_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='price_per_item',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Kaina už vnt.'),
        ),
    ]