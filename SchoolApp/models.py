from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from jsonfield import JSONField
# from django.contrib.postgres.fields import JSONField
# from djmoney.models.fields import MoneyField # pip install django-moneyfield
# from phone_field import PhoneField # pip install django-phone-field
# phone = PhoneField(blank=True, help_text='Contact phone number')
from phonenumber_field.modelfields import PhoneNumberField


# pip install django-phonenumber-field,phonenumbers

# Create your models here.


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    doj = models.DateField()
    # subjects = JSONField(default=list)
    salary = models.PositiveIntegerField()
    takes_web_lecture = models.BooleanField(default=False)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    doj = models.DateField()
    standard = models.CharField(max_length=20)
    roll_no = models.PositiveSmallIntegerField()
    ranking = models.PositiveSmallIntegerField()
    # subjects = JSONField(default=list)


class StudentsPointOfContact(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    relatives_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null=False, blank=False)
    RELATIONSHIP_CHOICES = [
        ("F", "Father"),
        ("M", "Mother"),
        ("S", "Sister"),
        ("B", "Brother"),
        ("U", "Uncle"),
        ("A", "Aunt")
    ]
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES, default='F')


class Classroom(models.Model):
    classroom_id = models.AutoField(primary_key=True)
    seating_capacity = models.PositiveSmallIntegerField()
    web_lecture_support = models.BooleanField(default=False)
    CLASS_CHOICES = [
        ("O", "Oval"),
        ("R", "Rectangular"),
        ("C", "Canopy"),
        ("E", "Elevated")
    ]
    shape = models.CharField(max_length=1, choices=CLASS_CHOICES, default='R')


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chapters = JSONField(default=list)
    total_duration = models.PositiveSmallIntegerField()
    per_class_duration = models.PositiveSmallIntegerField(validators=[MinValueValidator(30), MaxValueValidator(120)])


class TeacherSubjectMapping(models.Model):
    teacher_subject_mapping_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class StudentSubjectMapping(models.Model):
    student_subject_mapping_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class StudentSubjectTeacherMapping(models.Model):
    student_subject_teacher_mapping_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
