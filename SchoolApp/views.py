from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import *
import json, datetime


@csrf_exempt
@require_http_methods(["GET"])
def index(request):
    # return render(request, 'home.html', {})
    return render(request, "show.html", {})


@csrf_exempt
@require_http_methods(["GET"])
def get_teachers(request):
    # response = list(Teacher.objects.values())
    # return JsonResponse(response, safe=False)
    teachers = TeacherSubjectMapping.objects.all()
    return render(request, "showTeachers.html", {'teachers': teachers})


@csrf_exempt
@require_http_methods(["GET"])
def get_students(request):
    # response = list(Student.objects.values())
    # response = list(Student.objects.all().prefetch_related('student').values())
    # response = list(Student.objects.get(student_id=2).prefetch_related('students_point_of_contact'))
    # response = list(Student.objects.all().prefetch_related('students_point_of_contact').values())
    # response = list(Student.objects.select_related('students_point_of_contact').values())
    # response.append(list(Student.objects.get(student_id=3).studentspointofcontact_set.all().values()))
    # StudentsPointOfContact.objects.filter(student=3)
    # StudentsPointOfContact.objects.get(student=3).studentspointofcontact_set.all()
    # return JsonResponse(response, safe=False)
    # student_obj = Student.objects.get(student_id=1)
    # response = list(Student.objects.filter(student_id=1, studentspointofcontact__student=student_obj).values())
    # response = list(Student.objects.all().values())
    # val = list(Student.objects.select_related().values())
    # print(val)
    students = StudentSubjectMapping.objects.all()
    # for student in students:
    #     print(student.student.name, student.relatives_name)
    return render(request, "showStudents.html", {'students': students})


@csrf_exempt
@require_http_methods(["GET"])
def get_classrooms(request):
    response = list(Classroom.objects.values())
    # return JsonResponse(response, safe=False)
    return render(request, "showClassrooms.html", {'classrooms': response})


@csrf_exempt
@require_http_methods(["GET"])
def get_subjects(request):
    response = list(Subject.objects.values())
    # return JsonResponse(response, safe=False)
    return render(request, "showSubjects.html", {'subjects': response})


@csrf_exempt
@require_http_methods(["GET"])
def get_student_poc(request, student_id):
    response = list(StudentsPointOfContact.objects.filter(student=student_id).values())
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(["GET"])
def get_student_pocs(request):
    response = list(StudentsPointOfContact.objects.values())
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def create_teacher(request):
    req = json.loads(request.body.decode('utf-8'))
    name = req["name"]
    doj = req["doj"]
    subjects = req["subjects"]
    salary = req["salary"]
    takes_web_lecture = req["takes_web_lecture"]
    teacher = Teacher(name=name, doj=doj, salary=salary, takes_web_lecture=takes_web_lecture)
    teacher.save()
    for subject in subjects:
        subject_ob = Subject.objects.get(name=subject)
        teacher_subject_mapping = TeacherSubjectMapping(teacher=teacher, subject=subject_ob)
        teacher_subject_mapping.save()
    return HttpResponse(teacher.teacher_id)


@csrf_exempt
@require_http_methods(["POST"])
def create_student(request):
    req = json.loads(request.body.decode('utf-8'))
    name = req["name"]
    doj = req["doj"]
    standard = req["standard"]
    roll_no = req["roll_no"]
    ranking = req["ranking"]
    subjects = req["subjects"]
    student = Student(name=name, doj=doj, standard=standard, roll_no=roll_no, ranking=ranking)
    student.save()
    for subject in subjects:
        subject_ob = Subject.objects.get(name=subject)
        student_subject_mapping = StudentSubjectMapping(student=student, subject=subject_ob)
        student_subject_mapping.save()
    return HttpResponse(student.student_id)


@csrf_exempt
@require_http_methods(["POST"])
def create_classroom(request):
    req = json.loads(request.body.decode('utf-8'))
    seating_capacity = req["seating_capacity"]
    web_lecture_support = req["web_lecture_support"]
    shape = req["shape"]
    classroom = Classroom(seating_capacity=seating_capacity, web_lecture_support=web_lecture_support, shape=shape)
    classroom.save()
    return HttpResponse(classroom.classroom_id)


@csrf_exempt
@require_http_methods(["POST"])
def create_subject(request):
    req = json.loads(request.body.decode('utf-8'))
    name = req["name"]
    chapters = req["chapters"]
    total_duration = req["total_duration"]
    per_class_duration = req["per_class_duration"]
    subject = Subject(name=name, chapters=chapters, total_duration=total_duration,
                      per_class_duration=per_class_duration)
    subject.save()
    return HttpResponse(subject.subject_id)


@csrf_exempt
@require_http_methods(["POST"])
def create_student_poc(request, student_id):
    req = json.loads(request.body.decode('utf-8'))
    relatives_name = req["relatives_name"]
    phone_number = req["phone_number"]
    relationship = req["relationship"]
    try:
        student_obj = Student.objects.get(student_id=student_id)
    except Exception as e:
        return HttpResponse("The given student does not exist")
    students_point_of_contact = StudentsPointOfContact(student=student_obj,
                                                       relatives_name=relatives_name,
                                                       phone_number=phone_number, relationship=relationship)
    students_point_of_contact.save()
    return HttpResponse(students_point_of_contact.student_id)


@csrf_exempt
@require_http_methods(["GET"])
def delete_teachers(request):
    data = Teacher.objects.all()
    if data.exists():
        data.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Not Found")


@csrf_exempt
@require_http_methods(["GET"])
def delete_students(request):
    data = Student.objects.all()
    if data.exists():
        data.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Not Found")


@csrf_exempt
@require_http_methods(["GET"])
def delete_classrooms(request):
    data = Classroom.objects.all()
    if data.exists():
        data.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Not Found")


@csrf_exempt
@require_http_methods(["GET"])
def delete_subjects(request):
    data = Subject.objects.all()
    if data.exists():
        data.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Not Found")


@csrf_exempt
@require_http_methods(["GET"])
def delete_student_poc(request, student_id):
    data = StudentsPointOfContact.objects.filter(student=student_id)
    if data.exists():
        data.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Not Found")


@csrf_exempt
@require_http_methods(["GET"])
def delete_student_pocs(request):
    data = StudentsPointOfContact.objects.all()
    if data.exists():
        data.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse("Not Found")


@csrf_exempt
@require_http_methods(["POST"])
def assign_teachers(request, student_id):
    student_obj = Student.objects.get(student_id=student_id)
    student_subjects = list(StudentSubjectMapping.objects.filter(student=student_obj).values())
    # print("student_subjects", student_subjects)
    for student_subject in student_subjects:
        subject_obj = Subject.objects.get(subject_id=student_subject["subject_id"])
        # print("subject_obj", subject_obj)
        teachers = list(TeacherSubjectMapping.objects.filter(subject=subject_obj).values())
        # print("teachers", teachers)
        if len(teachers) > 1:
            # oldest = datetime.datetime.now()
            # present = datetime.datetime.now()
            # for teacher in teachers:
            #     doj = Teacher.objects.get(teacher_id=teacher["teacher_id"])[0]["doj"]
            #     if (present-doj) < oldest:
            #         oldest = present-doj
            teacher_obj = Teacher.objects.get(teacher_id=teachers[0]["teacher_id"])
        else:
            teacher_obj = Teacher.objects.get(teacher_id=teachers[0]["teacher_id"])
        # print("teacher_obj", teacher_obj)
        student_subject_teacher_mapping = StudentSubjectTeacherMapping(student=student_obj, subject=subject_obj, teacher=teacher_obj)
        student_subject_teacher_mapping.save()
        response = {}
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(["GET"])
def get_student_teacher_assignment(request):
    teachers = StudentSubjectTeacherMapping.objects.all()
    return render(request, "showStudentTeacherAssignment.html", {'teachers': teachers})
