from django.urls import path
from . import views


urlpatterns = [

    # ================================
    # Dashboard
    # ================================
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    # ================================
    # Students
    # ================================
    path(
        "list/",
        views.student_list,
        name="student_list"
    ),

    # Add Student
    path(
        "add/",
        views.add_student,
        name="add_student"
    ),

    # Edit Student
    path(
        "edit/<int:id>/",
        views.edit_student,
        name="edit_student"
    ),

    # Delete Student
    path(
        "delete/<int:id>/",
        views.delete_student,
        name="delete_student"
    ),

    # Student Details
    path(
        "detail/<int:id>/",
        views.student_detail,
        name="student_details"
    ),

    # ================================
    # Authentication
    # ================================
    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),
]