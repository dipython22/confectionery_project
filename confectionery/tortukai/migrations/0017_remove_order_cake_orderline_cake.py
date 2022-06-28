# Generated by Django 4.0.4 on 2022-06-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0016_order_order_date_alter_orderline_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cake',
        ),
        migrations.AddField(
            model_name='orderline',
            name='cake',
            field=models.ManyToManyField(related_name='order_lines', to='tortukai.cake', verbose_name='tortas'),
        ),
    ]