# Generated by Django 2.2.5 on 2021-02-13 09:20

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0010_auto_20210213_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=jsonfield.fields.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentspointofcontact',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Student'),
        ),
    ]
