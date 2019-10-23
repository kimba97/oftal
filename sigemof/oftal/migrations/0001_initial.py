# Generated by Django 2.0.13 on 2019-10-22 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=50)),
                ('tamano', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Aro',
                'verbose_name': 'Aro',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horaI', models.CharField(max_length=10)),
                ('horaF', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Citas',
                'verbose_name': 'Cita',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('diag', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Consultas',
                'verbose_name': 'Consulta',
            },
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumExp', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Expedientes',
                'verbose_name': 'Expediente',
            },
        ),
        migrations.CreateModel(
            name='FacturaAro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.FloatField(null=True)),
                ('total', models.FloatField(null=True)),
                ('cantidad', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacturaVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoFactura', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('precioVenta', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('aro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oftal.Aro')),
            ],
            options={
                'verbose_name_plural': 'FacturaVentas',
                'verbose_name': 'FacturaVenta',
            },
        ),
        migrations.CreateModel(
            name='Lente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('esfera', models.CharField(max_length=20)),
                ('cilindro', models.CharField(max_length=20)),
                ('eje', models.CharField(max_length=20)),
                ('prisma', models.CharField(max_length=20)),
                ('base', models.CharField(max_length=20)),
                ('adicion', models.CharField(max_length=20)),
                ('graduacion', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
                ('codigod', models.CharField(max_length=20)),
                ('esferad', models.CharField(max_length=20)),
                ('cilindrod', models.CharField(max_length=20)),
                ('ejed', models.CharField(max_length=20)),
                ('prismad', models.CharField(max_length=20)),
                ('based', models.CharField(max_length=20)),
                ('adiciond', models.CharField(max_length=20)),
                ('graduaciond', models.CharField(max_length=20)),
                ('colord', models.CharField(max_length=30)),
                ('factura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.FacturaAro')),
            ],
            options={
                'verbose_name_plural': 'Lentes',
                'verbose_name': 'Lente',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=200)),
                ('apellidoPersona', models.CharField(max_length=200)),
                ('dui', models.CharField(max_length=10, unique=True)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=9)),
                ('fechaNac', models.DateTimeField()),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Personas',
                'verbose_name': 'Persona',
                'permissions': (('isDoctora', 'Es Doctora'), ('isSecretaria', 'Es Secretaria')),
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oftal.Persona')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('nombrePadre', models.CharField(blank=True, max_length=20, null=True)),
                ('nombreMadre', models.CharField(blank=True, max_length=200, null=True)),
                ('remitente', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
                'verbose_name': 'Paciente',
            },
            bases=('oftal.persona',),
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oftal.Persona')),
                ('isss', models.CharField(max_length=12, unique=True)),
                ('afp', models.CharField(max_length=9, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Secretarias',
                'verbose_name': 'Secretaria',
            },
            bases=('oftal.persona',),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='lente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oftal.Lente'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='expedientePac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.Expediente'),
        ),
        migrations.CreateModel(
            name='Doctora',
            fields=[
                ('secretaria_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oftal.Secretaria')),
                ('jvpm', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Doctoras',
                'verbose_name': 'Doctora',
            },
            bases=('oftal.secretaria',),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oftal.Paciente'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.Paciente'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciCita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.Paciente'),
        ),
    ]
