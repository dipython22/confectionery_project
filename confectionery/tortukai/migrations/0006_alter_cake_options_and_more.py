# Generated by Django 4.0.3 on 2022-06-19 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0005_alter_order_options_alter_cake_cake_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cake',
            options={'ordering': ['cake_name'], 'verbose_name': 'tortas', 'verbose_name_plural': 'tortai'},
        ),
        migrations.RenameField(
            model_name='cake',
            old_name='cake_description',
            new_name='description',
        ),
    ]