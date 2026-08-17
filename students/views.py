from django.shortcuts import render, redirect, get_object_or_404

from .models import Student
from .forms import StudentForm

from courses.models import Course


# ================================
# Dashboard
# ================================

def dashboard(request):

    total_students = Student.objects.count()

    total_courses = Course.objects.count()

    recent_students = (
        Student.objects
        .select_related("course")
        .order_by("-id")[:5]
    )

    return render(
        request,
        "students/dashboard.html",
        {
            "total_students": total_students,
            "total_courses": total_courses,
            "recent_students": recent_students,
        }
    )


# ================================
# Student List
# ================================

def student_list(request):

    query = request.GET.get("q", "").strip()

    if query:

        students = (
            Student.objects
            .select_related("course")
            .filter(
                name__icontains=query
            )
            | Student.objects
            .select_related("course")
            .filter(
                email__icontains=query
            )
            | Student.objects
            .select_related("course")
            .filter(
                course__name__icontains=query
            )
        )

    else:

        students = (
            Student.objects
            .select_related("course")
            .all()
        )

    return render(
        request,
        "students/student_list.html",
        {
            "students": students,
            "query": query,
        }
    )


# ================================
# Add Student
# ================================

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form,
        }
    )


# ================================
# Edit Student
# ================================

def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect("student_list")

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        "students/edit_student.html",
        {
            "form": form,
            "student": student,
        }
    )


# ================================
# Delete Student
# ================================

def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        student.delete()

        return redirect("student_list")

    return render(
        request,
        "students/delete_student.html",
        {
            "student": student,
        }
    )


# ================================
# Student Details
# ================================

def student_detail(request, id):

    student = get_object_or_404(
        Student.objects.select_related("course"),
        id=id
    )

    return render(
        request,
        "students/student_details.html",
        {
            "student": student,
        }
    )