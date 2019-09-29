# Generated by Django 2.0.13 on 2019-09-29 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oftal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaLente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.FloatField(null=True)),
                ('total', models.FloatField(null=True)),
                ('cantidad', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='aro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.Lente'),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='codigoFactura',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='lente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.Cristal'),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.Paciente'),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='precioVenta',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='facturaventa',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='cristal',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oftal.FacturaLente'),
        ),
    ]
