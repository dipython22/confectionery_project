# Generated by Django 4.0.3 on 2022-06-19 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tortukai', '0004_alter_order_options_alter_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['deadline'], 'verbose_name': 'užakymą', 'verbose_name_plural': 'užsakymai'},
        ),
        migrations.AlterField(
            model_name='cake',
            name='cake_description',
            field=models.TextField(default='Aprašymas ruošiamas', max_length=1000, verbose_name='trumas aprašymas'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='occasion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='tortukai.occasion', verbose_name='tinka progai'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.IntegerField(default=370, verbose_name='tel.nr.:'),
        ),
    ]