# Generated by Django 2.2.5 on 2021-02-13 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0019_auto_20210213_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsubjectteachermapping',
            name='id',
        ),
        migrations.RemoveField(
            model_name='studentsubjectteachermapping',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='studentsubjectteachermapping',
            name='subject_id',
        ),
        migrations.RemoveField(
            model_name='studentsubjectteachermapping',
            name='teacher_id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AddField(
            model_name='studentsubjectteachermapping',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsubjectteachermapping',
            name='student_subject_teacher_mapping_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsubjectteachermapping',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsubjectteachermapping',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Teacher'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TeacherSubjectMapping',
            fields=[
                ('teacher_subject_mapping_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubjectMapping',
            fields=[
                ('student_subject_mapping_id', models.AutoField(primary_key=True, serialize=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.Subject')),
            ],
        ),
    ]