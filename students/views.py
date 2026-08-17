from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def dashboard(request):
    students = Student.objects.all()

    total_students = students.count()

    courses = students.values("course").distinct().count()

    recent_students = students.order_by("-id")[:5]

    return render(request, "students/dashboard.html", {
        "total_students": total_students,
        "total_courses": courses,
        "recent_students": recent_students,
    })


def student_list(request):
    students = Student.objects.all()

    return render(request, "students/student_list.html", {
        "students": students
    })


def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(request, "students/add_student.html", {
        "form": form
    })


def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(request, "students/edit_student.html", {
        "form": form,
        "student": student
    })


def delete_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "students/delete_student.html", {
        "student": student
    })