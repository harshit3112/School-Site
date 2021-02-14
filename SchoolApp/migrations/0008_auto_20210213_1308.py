# Generated by Django 2.2.5 on 2021-02-13 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0007_auto_20210210_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentspointofcontact',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_point_of_contact', to='SchoolApp.Student'),
        ),
    ]
