from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def student_list(request):
    # Get all students from the database
    students = Student.objects.all()

    # Send the student data to the HTML template
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