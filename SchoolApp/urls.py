from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('getTeachers', views.get_teachers, name='getTeachers'),
    path('getStudents', views.get_students, name='getStudents'),
    path('getClassrooms', views.get_classrooms, name='getClassrooms'),
    path('getSubjects', views.get_subjects, name='getSubjects'),
    path('getStudentPOC/<student_id>', views.get_student_poc, name='getStudentPOC'),
    path('getStudentPOCs', views.get_student_pocs, name='getStudentPOCs'),

    path('createTeacher', views.create_teacher, name='createTeacher'),
    path('createStudent', views.create_student, name='createStudent'),
    path('createClassroom', views.create_classroom, name='createClassroom'),
    path('createSubject', views.create_subject, name='createSubject'),
    path('createStudentPOC/<student_id>', views.create_student_poc, name='createStudentPOC'),

    path('deleteTeachers', views.delete_teachers, name='deleteTeachers'),
    path('deleteStudents', views.delete_students, name='deleteStudents'),
    path('deleteClassrooms', views.delete_classrooms, name='deleteClassrooms'),
    path('deleteSubjects', views.delete_subjects, name='deleteSubjects'),
    path('deleteStudentPOC/<student_id>', views.delete_student_poc, name='deleteStudentPOC'),
    path('deleteStudentPOCs', views.delete_student_pocs, name='deleteStudentPOCs'),

    path('assignTeachers/<student_id>', views.assign_teachers, name='assignTeachers'),
    path('getStudentTeacherAssignment', views.get_student_teacher_assignment, name='getStudentTeacherAssignment'),

]