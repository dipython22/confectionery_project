# Generated by Django 4.0.3 on 2022-06-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0027_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateField(db_index=True, verbose_name='pagaminti datai: '),
        ),
    ]
