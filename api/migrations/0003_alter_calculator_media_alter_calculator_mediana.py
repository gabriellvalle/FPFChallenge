# Generated by Django 5.2.1 on 2025-05-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_calculator_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='media',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='mediana',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
