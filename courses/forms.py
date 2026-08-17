from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = [
            "name",
            "description",
            "duration",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter course name"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter course description",
                    "rows": 4,
                }
            ),

            "duration": forms.NumberInput(
                attrs={
                    "placeholder": "Duration in months",
                    "min": 1,
                }
            ),
        }