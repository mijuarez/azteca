# Generated by Django 3.2.12 on 2022-04-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0010_alter_prospecters_birthplace'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prospecters',
            options={'verbose_name': 'Prospecto', 'verbose_name_plural': 'Prospectos'},
        ),
        migrations.AddField(
            model_name='prospecters',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='NOTAS'),
        ),
        migrations.AddField(
            model_name='prospecters',
            name='status',
            field=models.CharField(choices=[('PROSPECTO', 'PROSPECTO'), ('INSCRITO', 'INSCRITO')], default='INSCRITO', max_length=10, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='agreement',
            field=models.BooleanField(default=True, verbose_name='Convenio'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='birthplace',
            field=models.CharField(choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('Ciudad de México', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Michoacán', 'Michoacán'), ('México', 'México'), ('Morelos', 'Morelos'), ('NAYARIT', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='Jalisco', max_length=30, verbose_name='Lugar de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='campus',
            field=models.CharField(max_length=30, verbose_name='Plantel'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='company',
            field=models.CharField(max_length=50, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='curp',
            field=models.CharField(max_length=18, verbose_name='CURP'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='day',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='educational_options',
            field=models.CharField(max_length=30, verbose_name='Oferta Educativa'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='enrollment',
            field=models.BooleanField(default=True, verbose_name='Inscripción'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='gender',
            field=models.CharField(choices=[('HOMBRE', 'HOMBRE'), ('MUJER', 'MUJER')], default='HOMBRE', max_length=6, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='lastname_student',
            field=models.CharField(max_length=30, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='mother_lastname_student',
            field=models.CharField(max_length=30, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='movil',
            field=models.CharField(max_length=10, verbose_name='Teléfono Móvil'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='name_student',
            field=models.CharField(max_length=50, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='payment_enrollment',
            field=models.IntegerField(verbose_name='Monto de Inscripción'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='payment_period',
            field=models.CharField(choices=[('SEMANAL', 'SEMANAL'), ('MENSUAL', 'MENSUAL')], default='SEMANAL', max_length=8, verbose_name='Colegiatura'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='payment_period_amount',
            field=models.IntegerField(verbose_name='Monto de Colegiatura'),
        ),
        migrations.AlterField(
            model_name='prospecters',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Horario'),
        ),
    ]
