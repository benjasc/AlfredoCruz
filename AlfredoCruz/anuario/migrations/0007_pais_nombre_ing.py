# Generated by Django 2.0.4 on 2018-05-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuario', '0006_auto_20180529_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='nombre_ing',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
