# Generated by Django 2.0.4 on 2018-04-22 23:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RadioApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
