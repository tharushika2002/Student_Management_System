from django.shortcuts import render
from .models import Student


def student_list(request):
    # Get all students from the database
    students = Student.objects.all()

    # Send the student data to the HTML template
    return render(request, "students/student_list.html", {
        "students": students
    })