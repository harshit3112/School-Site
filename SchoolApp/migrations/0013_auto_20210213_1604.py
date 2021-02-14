# Generated by Django 2.2.5 on 2021-02-13 10:34

import django.core.validators
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0012_auto_20210213_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='chapters',
            field=jsonfield.fields.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='per_class_duration',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
