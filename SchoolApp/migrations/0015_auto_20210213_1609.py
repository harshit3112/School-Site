# Generated by Django 2.2.5 on 2021-02-13 10:39

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0014_auto_20210213_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=jsonfield.fields.JSONField(default=list),
        ),
    ]
