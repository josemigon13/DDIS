# Generated by Django 3.2.9 on 2021-11-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='NumSegSocial',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='Tlf_Empleado',
            field=models.IntegerField(),
        ),
    ]
