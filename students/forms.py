from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            "name",
            "email",
            "age",
            "course",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter student name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter email address"
                }
            ),

            "age": forms.NumberInput(
                attrs={
                    "placeholder": "Enter age",
                    "min": 1,
                }
            ),

            "course": forms.Select(
                attrs={
                    "class": "course-select"
                }
            ),
        }