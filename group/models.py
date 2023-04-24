from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, null=False)
    teacher_name = models.ForeignKey('user.User', null=False, on_delete=models.CASCADE)
    time_lesson = models.CharField(max_length=100, null=False)
    center_id = models.ForeignKey('center.Center', null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name