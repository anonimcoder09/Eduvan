from django.db import models

class StudentDates(models.Model):
    user_id = models.ForeignKey('student.Student', on_delete=models.CASCADE, null=False)
    is_there = models.BooleanField(null=False)
    date = models.DateTimeField(auto_now=True)