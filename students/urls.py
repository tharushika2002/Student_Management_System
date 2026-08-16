from django.urls import path
from . import views


urlpatterns = [
    # URL for displaying all students
    path("", views.student_list, name="student_list"),
]
