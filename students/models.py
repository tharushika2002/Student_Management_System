from django.db import models
class Student(models.Model):
    # Student's full name
    name = models.CharField(max_length=100)

    # Student's email address
    email = models.EmailField()

    # Student's age
    age = models.IntegerField()

    # Student's course name
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name