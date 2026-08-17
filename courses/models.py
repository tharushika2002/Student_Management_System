from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    duration = models.IntegerField(
        help_text="Duration in months"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name