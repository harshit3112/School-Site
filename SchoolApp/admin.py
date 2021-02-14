from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentsPointOfContact)
admin.site.register(Classroom)
admin.site.register(Subject)

admin.site.register(StudentSubjectMapping)
admin.site.register(TeacherSubjectMapping)
admin.site.register(StudentSubjectTeacherMapping)
