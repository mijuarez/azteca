# Generated by Django 3.2.12 on 2022-04-06 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import prospects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospecters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=50)),
                ('lastname_student', models.CharField(max_length=30)),
                ('mother_lastname_student', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('H', 'H'), ('M', 'M')], default='H', max_length=2)),
                ('birthplace', models.CharField(choices=[('JAL', 'JAL'), ('MICH', 'MICH'), ('NAY', 'NAY')], default='JAL', max_length=30)),
                ('educational_options', models.CharField(max_length=30)),
                ('campus', models.CharField(max_length=30)),
                ('time', models.CharField(default=prospects.models.get_default_my_hour, max_length=15)),
                ('day', models.CharField(max_length=15)),
                ('movil', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=255)),
                ('agreement', models.BooleanField(default=True)),
                ('company', models.CharField(max_length=50)),
                ('enrollment', models.CharField(max_length=2)),
                ('payment_enrollment', models.IntegerField()),
                ('payment_period', models.CharField(choices=[('SEMANAL', 'S'), ('MENSUAL', 'M')], default='SEMANAL', max_length=8)),
                ('payment_period_amount', models.IntegerField()),
                ('curp', models.CharField(max_length=18)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
