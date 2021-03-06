# Generated by Django 2.0.5 on 2018-05-29 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anuario', '0008_auto_20180529_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fondo',
            name='domicilio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anuario.domicilio'),
        ),
        migrations.AlterField(
            model_name='fondo',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fondo',
            name='moneda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anuario.moneda'),
        ),
    ]
