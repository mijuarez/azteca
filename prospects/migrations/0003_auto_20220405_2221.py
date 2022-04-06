# Generated by Django 3.2.12 on 2022-04-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0002_alter_prospecters_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospecters',
            name='birthplace',
            field=models.CharField(choices=[('JALISCO', 'JALISCO'), ('MICHOACAN', 'MICHOACAN'), ('NAYARIT', 'NAYAYARI')], default='JALISCO', max_length=30),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='gender',
            field=models.CharField(choices=[('HOMBRE', 'HOMBRE'), ('MUJER', 'MUJER')], default='HOMBRE', max_length=6),
        ),
    ]
