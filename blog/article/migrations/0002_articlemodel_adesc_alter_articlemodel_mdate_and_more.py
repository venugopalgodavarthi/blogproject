# Generated by Django 4.0.2 on 2022-02-26 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='adesc',
            field=models.TextField(default='yes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='mdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='pdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commments',
            name='cdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
