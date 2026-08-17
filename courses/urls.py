from django.urls import path

from . import views


urlpatterns = [
    path("",views.course_list, name="course_list"),
    path("add/",views.add_course,name="add_course"),
    path("edit/<int:id>/",views.edit_course,name="edit_course"),
    path("delete/<int:id>/",views.delete_course,name="delete_course"),
]