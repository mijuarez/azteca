# Generated by Django 3.2.12 on 2022-04-06 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0006_alter_prospecters_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospecters',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
